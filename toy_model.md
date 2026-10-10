# Toy model results — the computational round (round 4)

This is the first round of this project to actually compute anything, rather
than argue from literature and logic alone. Three scripts, three questions,
run with Python/NumPy/SciPy (no QuTiP — not installed, hand-built instead):

```
toy_model_detector_recorder.py  → does A collapse exactly where Θ becomes
                                   well-defined, as round 3 warned?
toy_model_tape_recorder.py      → does a renewable recorder fix it
                                   (operationalizing condition c)?
toy_model_qrf_invariant.py      → does de la Hamette's diagonal Rényi
                                   invariant rescue condition (b2)?
```

All code, CSV outputs, and this writeup are in the repo so results can be
reproduced or challenged directly — `python3 toy_model_detector_recorder.py`
etc. reruns everything from scratch in under a minute.

## 1. The detector-only model: round 3's structural warning, confirmed numerically

**Setup.** A two-level "detector" qubit D, standing in for an Unruh–DeWitt
detector undergoing uniform proper acceleration, modeled as an open quantum
system driven toward the Gibbs state at the Unruh temperature `T_U` by a
Markovian GKSL/Lindblad master equation with Bose–Einstein-weighted rates.
This is a standard, citable approximation technique for the Unruh effect's
thermalization behavior (confirmed via literature search this round — see
"Reliable quantum master equation of the Unruh-DeWitt detector," arXiv:
2502.06411 — not the full field-theoretic derivation, which is unnecessary
for testing the T/A/R/Θ coincidence question itself). A second qubit R
("recorder") is coupled to D but *not* to the bath directly, under two
different coupling Hamiltonians: an excitation-conserving swap coupling
(chosen because it commutes with `H_D`, the natural candidate operationalization
of condition (c)'s "couples to the modular generator") and a non-commuting
`σ_x⊗σ_x` coupling, for contrast.

**Result.** D's fidelity to its Gibbs/KMS state hits ≈1.0 almost immediately
(by `τ≈2`, in units where the bath relaxation rate `Γ0=1`) — Θ becomes
well-defined essentially right away, for both couplings. But exactly as
round 3's holistic review warned: the numerically-computed entropy
production and the mutual information `I(D:R)` both *peak early and then
decay* toward zero as `τ→∞` (down to `0.00044` and `0.00025` nats by
`τ=150`, for the swap coupling, still visibly shrinking). **The round-3
concern was not just a plausible theoretical worry — it is what the model
actually does.** A single static recorder cannot sustain nonzero A and R
once the whole D+R system settles toward its own joint equilibrium, even
though D's local KMS-ness (hence Θ) was secured almost immediately.

A Spohn-type non-negativity check (entropy production ≥ 0, since a KPV-style
functional is supposed to be a legitimate dissipation measure) was run
numerically across every timestep of every run: minimum observed value was
`~1e-6` (consistent with zero, within numerical noise), never negative. This
doesn't prove the inequality in general, but the toy model didn't violate it.

## 2. The "tape" extension: operationalizing condition (c)

**What changed.** Round 3 had already connected this exact physics to Erker
et al.'s autonomous-clock literature, which uses a semi-infinite stream of
fresh ancillas ("ticks") rather than a single fixed recorder (this is a
standard architecture in quantum thermodynamics — "collision models" /
repeated-interaction schemes; Ciccarello, Lorenzo, Giovannetti & Palma,
Phys. Rep. 954, 1–70 (2022), arXiv:2106.11974 — verified this round). So:
replace the static recorder with one that gets reset to a fresh ground state
every `Δτ_reset = 8` time units, keeping D's own marginal exactly as the
dynamics left it (a "swap in fresh tape" operation).

**Result — this is the project's cleanest positive finding so far.** After
one initial transient cycle (dominated by D's own thermalization from its
starting ground state), *every subsequent cycle produces an exactly
repeating, constant amount* of entropy production and recorder mutual
information per cycle:

| Coupling | Entropy produced / cycle | Mutual-info gained / cycle | D's fidelity to Gibbs throughout |
|---|---|---|---|
| swap (commutes with H_D) | 0.039005 nats | 0.002105 nats | 1.000000 (never dips, to printed precision) |
| σ_x⊗σ_x (does not commute) | 0.072245 nats | 0.003569 nats | 1.000000 (same) |

This held steady, to 6 decimal places, across all 25 simulated cycles for
both couplings — not an asymptotic approach, an exact lock-in after the
first cycle. **This directly operationalizes condition (c)**: the recording
apparatus must be a *renewable* degree of freedom (a tape, not a fixed
finite system) to sustain nonzero A and R indefinitely while Θ stays
well-defined throughout. That specific requirement was prose in
`framework.md` v2.2 ("recording apparatus couples to...") — it is now a
concrete, numerically demonstrated mechanism with a name from existing
literature (collision models) behind it.

**What this result does *not* yet distinguish:** the commuting (swap) and
non-commuting (`σ_x⊗σ_x`) couplings *both* worked, at these parameters —
fidelity stayed pinned at 1.0 either way, just with different rates. This
is the one place this round's numerics *failed* to validate the specific
form condition (c) was given in `framework.md` v2.2 (that the coupling must
commute with the modular generator). At this coupling strength
(`g=0.05 ≪ Γ0=1`), the bath's fast relaxation apparently suppresses D's
deviation from Gibbs regardless of which coupling is used — the commutation
requirement may only start to matter at larger `g/Γ0`, which was not swept.
**Open, not resolved**: condition (c) needs restating as a *quantitative*
threshold (how large can `g/Γ0` get before the non-commuting coupling
visibly disrupts D's KMS-ness?), not a qualitative commute/don't-commute
distinction — this toy model's parameter range was too conservative to
probe that boundary.

## 3. The QRF test: inconclusive, and said so rather than forced

**What was checked first, properly.** Before testing anything, de la
Hamette's actual theorem (arXiv:2603.23598) was fetched and read (not
guessed from the earlier round's paraphrase — see `self_critique.md` round
4): `S_α(Δρ_X^{(R_i)}) = S_α(Δρ_Y^{(R_j)})` for "ideal frames," where `Δ` is
full dephasing in the group-label basis, for `X,Y` related by the
frame-change permutation.

**Setup.** A minimal, self-built (not reproduced from any paper — the
source paper states its result only abstractly, with no worked example) 3-qubit
toy model: R1, R2 (two candidate reference frames), S (target system), under
a global Z2 (bit-flip) symmetry, with physical states restricted to the
symmetric (+1 eigenspace) sector. A "frame change to R_i" was implemented as
the standard conditional-flip construction (flip the other two qubits iff
`R_i=1`, then discard `R_i`).

**Result.** For a *restricted* 2-term family of states, raw and dephased
Rényi entropies of S both matched trivially across frames — but this turned
out to be a dead-end test: that restricted family has an accidental
`R1↔R2` exchange symmetry baked in, which would make the comparison match
for reasons unrelated to the cited theorem. For a *generic* 4-term family
(all four symmetric sectors populated), **neither the raw nor the dephased
Rényi entropies of S matched across frames**, for any of `α∈{0.5,1,2}`
tested.

**Conclusion — stated as what it actually is, not forced into a clean
answer.** This is **inconclusive, not a refutation of de la Hamette's
theorem.** Rényi entropy is already invariant under relabeling a diagonal
matrix's own entries, so "exists a permutation" (the theorem's actual
condition) can't explain away a mismatch in the *multiset* of diagonal
values, which is what was found. The most likely explanation is that this
project's simple conditional-flip toy construction does not fully satisfy
the formal "ideal frame" preconditions the theorem assumes (it may require
additional structure — e.g. the frame carrying a faithful regular
representation of the symmetry group, or a different definition of
"relational/relative state" than the simple conditional-unitary map used
here). **This was not chased further this round** — risk of compounding a
construction error into a false claim (either "the fix works" or "the fix
fails") was judged higher-value to flag and stop than to push through, per
this project's standing discipline against asserting unverified conclusions.

**What this round *did* establish, honestly:** the underlying QRF-relativity
problem itself — that the *raw* reduced state of the same physical subsystem
S genuinely differs depending on which of two systems is treated as "the
frame" — is not just a citation from Giacomini et al., it is now directly,
numerically reproduced in an explicit, checkable discrete toy case (the
raw-entropy mismatches in the trials table are real, computed numbers, not
an assertion). The proposed *fix* (diagonal Rényi invariants) remains
untested in any confirmed sense; condition (b2) is still open.

## What this round changes in `framework.md`'s Claim 2

1. Condition (c) can now be stated with a concrete, literature-grounded
   mechanism (renewable recorder / collision-model tape) instead of pure
   prose — but the specific "commutes with the modular generator" clause is
   *not yet distinguished from its absence* at the parameters tested, and
   needs restating as a quantitative (not qualitative) requirement.
2. Condition (b2)'s proposed fix (diagonal Rényi invariants) is **neither
   confirmed nor refuted** by this round — it needs either a more faithful
   reconstruction of de la Hamette's "ideal frame" formalism or a different
   toy model, before `framework.md` can say anything stronger than "open."
3. The A/KMS structural tension flagged in round 3 was not just a worry —
   this round's base-case simulation (section 1 above) shows it actually
   happening, which is useful independent confirmation that round 3's
   holistic read caught something real rather than a hypothetical concern.

## Honest status

Two of three sub-goals from the last `/goal` command produced a genuine,
checkable result (sections 1–2: condition (c) operationalized with a
working, numerically demonstrated fix, though not yet fully precise).
The third (testing the QRF fix) produced an honest "inconclusive" rather
than a forced answer either way — which is the correct outcome to report
when a toy model's own validity against the cited formalism couldn't be
confirmed in the time available, not a failure of the research process.
