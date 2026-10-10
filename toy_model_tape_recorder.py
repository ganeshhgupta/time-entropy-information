"""
Extension of toy_model_detector_recorder.py, triggered by what that script's
first run actually showed (not what was hypothesized going in): a single,
static recorder qubit R builds up mutual information with D only
transiently, then that correlation washes back out as D+R drift toward a
joint equilibrium, so both I(D:R) and the entropy-production rate decay
toward zero at late tau even though D's fidelity to its Gibbs/KMS state
(hence Theta's well-definedness) is already essentially perfect by tau~2.

Fix tested here, modeled as a repeated-interaction / "collision model"
(standard in quantum thermodynamics -- Ciccarello, Lorenzo, Giovannetti &
Palma, "Quantum collision models," Phys. Rep. 2022): replace the single
static recorder with a periodically refreshed one -- a stand-in for a
semi-infinite "tape" of fresh ancillas, exactly the architecture autonomous
quantum clocks actually use (Erker et al., PRX 2017, already cited in
framework.md) to keep ticking indefinitely instead of saturating.

Mechanism: every Delta_tau_reset, replace rho_R by a fresh |ground><ground|
while keeping rho_D's marginal exactly as the dynamics left it (a projective
"swap in fresh tape" operation). Check whether this sustains a nonzero,
repeating per-cycle entropy production and per-cycle mutual-information gain
indefinitely, while D's fidelity to its Gibbs state stays pinned near 1
throughout (i.e. Theta stays well-defined the whole time).
"""
import numpy as np
from scipy.linalg import expm, eigh
from scipy.integrate import solve_ivp

from toy_model_detector_recorder import (
    I2, sigma_z, sigma_plus, sigma_minus, kron,
    von_neumann_entropy, partial_trace_R, partial_trace_D,
    fidelity, dissipator,
)


def run_tape(coupling, omega_D, omega_R, T_U, Gamma0, g, reset_period, n_cycles, pts_per_cycle):
    n_bar = 1.0 / (np.exp(omega_D / T_U) - 1.0)
    Gamma_down = Gamma0 * (n_bar + 1.0)
    Gamma_up = Gamma0 * n_bar

    H_D_small = (omega_D / 2.0) * sigma_z
    H_D = kron(H_D_small, I2)
    H_R = kron(I2, (omega_R / 2.0) * sigma_z)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    if coupling == 'swap':
        H_int = g * (kron(sigma_plus, sigma_minus) + kron(sigma_minus, sigma_plus))
    elif coupling == 'xx':
        H_int = g * kron(sx, sx)
    elif coupling == 'zx':
        H_int = g * kron(sigma_z, sx)  # genuinely commutes with H_D alone, any omega
    else:
        raise ValueError(coupling)
    H = H_D + H_R + H_int
    Ld = kron(sigma_minus, I2)
    Lu = kron(sigma_plus, I2)

    rho_gibbs_D = expm(-H_D_small / T_U)
    rho_gibbs_D /= np.trace(rho_gibbs_D).real

    def rhs(t, y):
        rho = y.reshape(4, 4)
        drho = -1j * (H @ rho - rho @ H) + dissipator(rho, Ld, Lu, Gamma_down, Gamma_up)
        return drho.flatten()

    ground_R = np.array([[0, 0], [0, 1]], dtype=complex)
    rho_D = np.array([[0, 0], [0, 1]], dtype=complex)  # D starts in ground too
    rho_DR = kron(rho_D, ground_R)

    cycle_log = []
    full_trace = []
    t_global = 0.0

    for cycle in range(n_cycles):
        t_eval = np.linspace(0, reset_period, pts_per_cycle)
        sol = solve_ivp(rhs, (0, reset_period), rho_DR.flatten(), t_eval=t_eval,
                         method='RK45', rtol=1e-9, atol=1e-12)

        I_vals, S_D_vals, F_vals, ent_prod_vals = [], [], [], []
        for idx in range(len(t_eval)):
            rho = sol.y[:, idx].reshape(4, 4)
            rho = (rho + rho.conj().T) / 2
            rD = partial_trace_R(rho)
            rR = partial_trace_D(rho)
            S_D = von_neumann_entropy(rD)
            S_R = von_neumann_entropy(rR)
            S_DR = von_neumann_entropy(rho)
            I_DR = S_D + S_R - S_DR
            F = fidelity(rD, rho_gibbs_D)

            drho_dt = rhs(t_eval[idx], rho.flatten()).reshape(4, 4)
            diss = dissipator(rho, Ld, Lu, Gamma_down, Gamma_up)
            Qdot = float(np.trace(H_D @ diss).real)
            w, v = eigh(rho)
            w = np.clip(w.real, 1e-14, None)
            ln_rho = (v * np.log(w)) @ v.conj().T
            dS_dt = float(-np.trace(drho_dt @ ln_rho).real)
            sigma_prod = dS_dt - Qdot / T_U

            I_vals.append(I_DR); S_D_vals.append(S_D); F_vals.append(F)
            ent_prod_vals.append(sigma_prod)
            full_trace.append(dict(tau=t_global + t_eval[idx], cycle=cycle,
                                    S_D=S_D, I_DR=I_DR, fidelity_D_to_gibbs=F,
                                    entropy_production=sigma_prod))

        I_gain_this_cycle = I_vals[-1] - I_vals[0]
        ent_prod_integrated = np.trapz(ent_prod_vals, t_eval)
        cycle_log.append(dict(cycle=cycle, t_start=t_global,
                               I_gain=I_gain_this_cycle,
                               entropy_produced=ent_prod_integrated,
                               fidelity_min=min(F_vals), fidelity_max=max(F_vals)))

        # reset: keep D's marginal as the dynamics left it, swap in a fresh R
        rho_D_end = partial_trace_R(sol.y[:, -1].reshape(4, 4))
        rho_D_end = (rho_D_end + rho_D_end.conj().T) / 2
        rho_DR = kron(rho_D_end, ground_R)
        t_global += reset_period

    return cycle_log, full_trace, n_bar


if __name__ == '__main__':
    import csv

    for coupling in ['swap', 'xx', 'zx']:
        # g=2.0 (stronger than round 4's 0.05) deliberately chosen in the
        # regime where toy_model_detector_recorder.py's sweep showed xx's
        # fidelity-to-Gibbs visibly degrading (~0.969) while zx stayed exact.
        cycle_log, full_trace, n_bar = run_tape(
            coupling, omega_D=1.0, omega_R=1.0, T_U=1.0, Gamma0=1.0, g=2.0,
            reset_period=8.0, n_cycles=25, pts_per_cycle=120)

        with open(f'toy_model_tape_cycles_{coupling}.csv', 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(cycle_log[0].keys()))
            w.writeheader(); w.writerows(cycle_log)

        print(f"\n=== coupling={coupling} (n_bar={n_bar:.4f}) ===")
        print(f"{'cycle':>5} {'t_start':>8} {'I_gain':>10} {'entropy_produced':>17} "
              f"{'fid_min':>9} {'fid_max':>9}")
        for row in cycle_log:
            print(f"{row['cycle']:5d} {row['t_start']:8.1f} {row['I_gain']:10.6f} "
                  f"{row['entropy_produced']:17.6f} {row['fidelity_min']:9.6f} "
                  f"{row['fidelity_max']:9.6f}")
