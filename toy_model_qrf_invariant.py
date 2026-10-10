"""
Minimal, self-built (NOT a reproduction of any cited paper's own example --
de la Hamette arXiv:2603.23598 states its own result only at the abstract
group-theoretic level, with no worked example) test of whether a "diagonal
Rényi invariant" rescues Claim 2's condition (b2): the finding (round 1) that
raw mutual information / entropy for a FIXED subsystem still disagrees
between two different quantum reference frames (QRF) describing the same
physical state.

Definition actually used (fetched and verified directly from the paper via
WebFetch on 2026-10-10, not guessed -- see self_critique.md round 4):
  S_alpha(rho)            = 1/(1-alpha) * log Tr(rho^alpha)      [Renyi-alpha]
  Delta(rho)               = full dephasing in the group-label basis
  Theorem 1 (ideal frames): S_alpha(Delta rho_X^(Ri)) = S_alpha(Delta rho_Y^(Rj))
                              for X,Y related by the frame-change permutation.

Setup: three qubits R1, R2, S with global Z2 symmetry (simultaneous bit-flip
X(x)X(x)X). Physical states live in the +1 eigenspace of that symmetry
(the group-invariance constraint of the perspective-neutral/relational QRF
approach). R1 and R2 are each a candidate "ideal frame"; S is the target
system whose description we compare across frames.
"""
import numpy as np
from scipy.linalg import eigh

I2 = np.eye(2)
X = np.array([[0, 1], [1, 0]], dtype=complex)


def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)


def renyi_entropy(rho, alpha):
    rho = (rho + rho.conj().T) / 2
    evals = np.clip(eigh(rho, eigvals_only=True).real, 0, None)
    evals = evals[evals > 1e-13]
    if abs(alpha - 1.0) < 1e-9:
        return float(-np.sum(evals * np.log(evals)))
    return float(1.0 / (1.0 - alpha) * np.log(np.sum(evals ** alpha)))


def dephase_computational_basis(rho):
    return np.diag(np.diag(rho)).astype(complex)


def partial_trace(rho8, keep, dims=(2, 2, 2)):
    """keep: tuple of axis indices (0=R1,1=R2,2=S) to KEEP; traces out the rest."""
    rho = rho8.reshape(dims + dims)
    all_idx = [0, 1, 2]
    trace_idx = [i for i in all_idx if i not in keep]
    # build einsum string: bra indices a0a1a2, ket indices b0b1b2, trace where index in trace_idx
    letters_bra = ['a', 'b', 'c']
    letters_ket = ['d', 'e', 'f']
    bra = letters_bra[:]
    ket = letters_ket[:]
    for i in trace_idx:
        ket[i] = bra[i]  # force equal to trace
    in_str = ''.join(bra) + ''.join(ket)
    out_str = ''.join(bra[i] for i in keep) + ''.join(ket[i] for i in keep)
    result = np.einsum(f'{in_str}->{out_str}', rho)
    d = 2 ** len(keep)
    return result.reshape(d, d)


def build_state(theta):
    """Pi-invariant 3-qubit state: cos(theta)(|000>+|111>)/sqrt2 + sin(theta)(|001>+|110>)/sqrt2
    Qubit order: R1, R2, S."""
    psi = np.zeros(8, dtype=complex)
    idx = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    c, s = np.cos(theta) / np.sqrt(2), np.sin(theta) / np.sqrt(2)
    psi[idx['000']] += c
    psi[idx['111']] += c
    psi[idx['001']] += s
    psi[idx['110']] += s
    return psi


def build_general_state(c1, c2, c3, c4):
    """General Pi-invariant 3-qubit state using all four symmetric sectors:
    c1*(|000>+|111>) + c2*(|001>+|110>) + c3*(|010>+|101>) + c4*(|011>+|100>),
    each divided by sqrt(2), then normalized overall. Qubit order: R1,R2,S."""
    idx = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    psi = np.zeros(8, dtype=complex)
    pairs = [('000', '111'), ('001', '110'), ('010', '101'), ('011', '100')]
    for coeff, (x, xbar) in zip([c1, c2, c3, c4], pairs):
        psi[idx[x]] += coeff / np.sqrt(2)
        psi[idx[xbar]] += coeff / np.sqrt(2)
    psi /= np.linalg.norm(psi)
    return psi


def frame_change_unitary(control_qubit):
    """V = |0><0|_control (x) I  +  |1><1|_control (x) (X on the OTHER two qubits).
    control_qubit in {0 (R1), 1 (R2)}. Qubit order fixed as (R1,R2,S)."""
    P0 = np.array([[1, 0], [0, 0]], dtype=complex)
    P1 = np.array([[0, 0], [0, 1]], dtype=complex)
    if control_qubit == 0:  # control = R1, flip R2,S
        term0 = kron3(P0, I2, I2)
        term1 = kron3(P1, X, X)
    elif control_qubit == 1:  # control = R2, flip R1,S
        term0 = kron3(I2, P0, I2)
        term1 = kron3(X, P1, X)
    else:
        raise ValueError
    return term0 + term1


def relational_state_of_S(psi, frame):
    """frame='R1' or 'R2'. Apply the frame-change unitary controlled on that
    qubit, then trace out BOTH the (now-decoupled) control qubit and the
    other spectator qubit, returning only S's reduced relational state."""
    control_qubit = 0 if frame == 'R1' else 1
    V = frame_change_unitary(control_qubit)
    psi_rel = V @ psi
    rho_full = np.outer(psi_rel, psi_rel.conj())
    return partial_trace(rho_full, keep=(2,))  # keep S only (axis 2)


if __name__ == '__main__':
    rng = np.random.default_rng(42)
    print("Generic (all four symmetric sectors populated, random complex-ish coefficients):")
    print(f"{'trial':>5} {'alpha':>6} | {'S_raw(R1)':>11} {'S_raw(R2)':>11} {'raw match?':>11} | "
          f"{'S_deph(R1)':>12} {'S_deph(R2)':>12} {'deph match?':>12}")
    for trial in range(6):
        c = rng.normal(size=4) + 0j
        psi = build_general_state(*c)
        assert abs(np.vdot(psi, psi) - 1.0) < 1e-9, "state not normalized"

        rho_S_R1 = relational_state_of_S(psi, 'R1')
        rho_S_R2 = relational_state_of_S(psi, 'R2')

        for alpha in [1.0, 2.0, 0.5]:
            s_raw_1 = renyi_entropy(rho_S_R1, alpha)
            s_raw_2 = renyi_entropy(rho_S_R2, alpha)
            s_deph_1 = renyi_entropy(dephase_computational_basis(rho_S_R1), alpha)
            s_deph_2 = renyi_entropy(dephase_computational_basis(rho_S_R2), alpha)
            raw_match = abs(s_raw_1 - s_raw_2) < 1e-8
            deph_match = abs(s_deph_1 - s_deph_2) < 1e-8
            print(f"{trial:5d} {alpha:6.1f} | {s_raw_1:11.6f} {s_raw_2:11.6f} "
                  f"{str(raw_match):>11} | {s_deph_1:12.6f} {s_deph_2:12.6f} {str(deph_match):>12}")

    print("\nOriginal two-sector family (theta sweep) kept for reference:")
    print(f"{'theta':>8} {'alpha':>6} | {'S_raw(R1)':>11} {'S_raw(R2)':>11} {'raw match?':>11} | "
          f"{'S_deph(R1)':>12} {'S_deph(R2)':>12} {'deph match?':>12}")
    for theta_deg in [0, 15, 30, 45, 60, 75, 90]:
        theta = np.deg2rad(theta_deg)
        psi = build_state(theta)
        rho_S_R1 = relational_state_of_S(psi, 'R1')
        rho_S_R2 = relational_state_of_S(psi, 'R2')
        for alpha in [1.0, 2.0, 0.5]:
            s_raw_1 = renyi_entropy(rho_S_R1, alpha)
            s_raw_2 = renyi_entropy(rho_S_R2, alpha)
            s_deph_1 = renyi_entropy(dephase_computational_basis(rho_S_R1), alpha)
            s_deph_2 = renyi_entropy(dephase_computational_basis(rho_S_R2), alpha)
            raw_match = abs(s_raw_1 - s_raw_2) < 1e-8
            deph_match = abs(s_deph_1 - s_deph_2) < 1e-8
            print(f"{theta_deg:8d} {alpha:6.1f} | {s_raw_1:11.6f} {s_raw_2:11.6f} "
                  f"{str(raw_match):>11} | {s_deph_1:12.6f} {s_deph_2:12.6f} {str(deph_match):>12}")
