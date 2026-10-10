"""
Toy model: Unruh-DeWitt-type detector D (thermalizing toward the Unruh
temperature via a Markovian/Lindblad open-quantum-system approximation,
following the standard GKSL reduction used e.g. in arXiv:2502.06411) coupled
weakly to a separate recorder qubit R that does NOT touch the bath directly.

Purpose: give T (proper time), A (entropy production), R (mutual information
with a recorder), and Theta (modular/thermal time, well-defined only once D
is close to its KMS/Gibbs state) a single shared, numerically computable
playground, to test Claim 2 (framework.md section 3) concretely instead of
only arguing about it in prose.

Units: hbar = c = k_B = 1 throughout.
"""
import numpy as np
from scipy.linalg import expm, sqrtm, eigh

# ---------- building blocks ----------
I2 = np.eye(2, dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)      # |0>=excited(+1), |1>=ground(-1)
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_minus = np.array([[0, 0], [1, 0]], dtype=complex)   # excited -> ground
sigma_plus = np.array([[0, 1], [0, 0]], dtype=complex)    # ground -> excited


def kron(a, b):
    return np.kron(a, b)


def von_neumann_entropy(rho):
    evals = eigh(rho, eigvals_only=True)
    evals = np.clip(evals.real, 1e-14, None)
    return float(-np.sum(evals * np.log(evals)))


def partial_trace_R(rho4):
    """Trace out R (second qubit) from a 4x4 state ordered as D (x) R."""
    rho = rho4.reshape(2, 2, 2, 2)
    return np.einsum('ikjk->ij', rho)


def partial_trace_D(rho4):
    """Trace out D (first qubit) from a 4x4 state ordered as D (x) R."""
    rho = rho4.reshape(2, 2, 2, 2)
    return np.einsum('kikj->ij', rho)


def fidelity(rho, sigma):
    srho = sqrtm(rho)
    inner = srho @ sigma @ srho
    inner = (inner + inner.conj().T) / 2  # hermitize, kill numerical noise
    evals = np.clip(eigh(inner, eigvals_only=True).real, 0, None)
    return float(np.sum(np.sqrt(evals)) ** 2)


def dissipator(rho4, Ld, Lu, Gamma_down, Gamma_up):
    def lind(L, rho):
        LdagL = L.conj().T @ L
        return L @ rho @ L.conj().T - 0.5 * (LdagL @ rho + rho @ LdagL)
    return Gamma_down * lind(Ld, rho4) + Gamma_up * lind(Lu, rho4)


def run_case(label, omega_D, omega_R, T_U, Gamma0, g, coupling, tau_max, n_pts):
    n_bar = 1.0 / (np.exp(omega_D / T_U) - 1.0)
    Gamma_down = Gamma0 * (n_bar + 1.0)
    Gamma_up = Gamma0 * n_bar

    H_D_small = (omega_D / 2.0) * sigma_z
    H_D = kron(H_D_small, I2)
    H_R = kron(I2, (omega_R / 2.0) * sigma_z)

    if coupling == 'swap':
        H_int = g * (kron(sigma_plus, sigma_minus) + kron(sigma_minus, sigma_plus))
    elif coupling == 'xx':
        H_int = g * kron(sigma_x, sigma_x)
    else:
        raise ValueError(coupling)

    H = H_D + H_R + H_int
    Ld = kron(sigma_minus, I2)
    Lu = kron(sigma_plus, I2)

    rho_gibbs_D = expm(-H_D_small / T_U)
    rho_gibbs_D /= np.trace(rho_gibbs_D).real

    def rhs(tau, y):
        rho = y.reshape(4, 4)
        drho = -1j * (H @ rho - rho @ H) + dissipator(rho, Ld, Lu, Gamma_down, Gamma_up)
        return drho.flatten()

    # initial state: both qubits in ground state, no coherence, no correlation
    rho0 = np.zeros((4, 4), dtype=complex)
    rho0[3, 3] = 1.0  # |ground_D, ground_R><same| with basis order (D=0 excited,1 ground)

    from scipy.integrate import solve_ivp
    taus = np.linspace(0, tau_max, n_pts)
    sol = solve_ivp(rhs, (0, tau_max), rho0.flatten(), t_eval=taus,
                     method='RK45', rtol=1e-9, atol=1e-12)

    rows = []
    for idx, tau in enumerate(taus):
        rho_DR = sol.y[:, idx].reshape(4, 4)
        rho_DR = (rho_DR + rho_DR.conj().T) / 2
        rho_D = partial_trace_R(rho_DR)
        rho_R = partial_trace_D(rho_DR)

        S_D = von_neumann_entropy(rho_D)
        S_R = von_neumann_entropy(rho_R)
        S_DR = von_neumann_entropy(rho_DR)
        I_DR = S_D + S_R - S_DR  # leg R: recorded/mutual information

        F = fidelity(rho_D, rho_gibbs_D)  # how close D is to being KMS/Gibbs

        drho_dtau = rhs(tau, rho_DR.flatten()).reshape(4, 4)
        diss = dissipator(rho_DR, Ld, Lu, Gamma_down, Gamma_up)
        Qdot = float(np.trace(H_D @ diss).real)  # heat flow from bath into D

        evals_DR = np.clip(eigh(rho_DR, eigvals_only=True).real, 1e-14, None)
        # dS/dtau = -Tr[drho/dtau * ln(rho)] since Tr[drho/dtau] = 0
        w, v = eigh(rho_DR)
        w = np.clip(w.real, 1e-14, None)
        ln_rho = (v * np.log(w)) @ v.conj().T
        dS_DR_dtau = float(-np.trace(drho_dtau @ ln_rho).real)

        sigma_prod = dS_DR_dtau - Qdot / T_U  # numerically-checked entropy production

        rows.append(dict(tau=tau, S_D=S_D, S_R=S_R, S_DR=S_DR, I_DR=I_DR,
                          fidelity_D_to_gibbs=F, Qdot=Qdot,
                          dS_DR_dtau=dS_DR_dtau, entropy_production=sigma_prod))
    return rows, n_bar


if __name__ == '__main__':
    import csv

    params = dict(omega_D=1.0, omega_R=1.0, T_U=1.0, Gamma0=1.0, g=0.05,
                  tau_max=150.0, n_pts=600)

    for coupling in ['swap', 'xx']:
        rows, n_bar = run_case(coupling, coupling=coupling, **params)
        fname = f'toy_model_results_{coupling}.csv'
        with open(fname, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f'--- case={coupling} (n_bar={n_bar:.4f}) written to {fname} ---')
        for tau_target in [0, 2, 5, 10, 20, 50, 100, 149.75]:
            r = min(rows, key=lambda rr: abs(rr['tau'] - tau_target))
            print(f"tau={r['tau']:7.2f}  F(D,Gibbs)={r['fidelity_D_to_gibbs']:.5f}  "
                  f"S_D={r['S_D']:.4f}  I(D:R)={r['I_DR']:.5f}  "
                  f"entropy_prod={r['entropy_production']:+.6f}")
