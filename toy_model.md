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
well-defined essentially right away, at this weak coupling, for all
couplings tested. But exactly as round 3's holistic review warned: the
numerically-computed entropy production and the mutual information `I(D:R)`
both *peak early and then decay* toward zero as `τ→∞` (down to `0.000547`
and `0.00025` nats respectively by `τ=150`, for the swap coupling, still
visibly shrinking). **The round-3 concern was not just a plausible
theoretical worry — it is what the model actually does.** A single static
recorder cannot sustain nonzero A and R once the whole D+R system settles
toward its own joint equilibrium, even though D's local KMS-ness (hence Θ)
was secured almost immediately.

**Correction (round 5, after an adversarial code/physics audit — see
`self_critique.md`):** the entropy-production value at `τ=0` (`+18.18`) is a
regularization artifact from clipping near-zero eigenvalues before taking a
logarithm at an exact pure-state corner (it scales with `-ln(clip threshold)`
and has no well-defined limit) — not real physics. It does not affect any of
the steady-state numbers reported here or in section 2's post-cycle-0 table,
confirmed by checking that dropping the `τ=0` sample changes cycle-1's
integral by only 0.3%; it does inflate the originally-reported *cycle-0*
transient number in section 2 by roughly 3.8×, which is corrected below.

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

**Result (round 4, weak coupling `g=0.05`) — the project's first clean
positive finding.** After one initial transient cycle (dominated by D's own
thermalization from its starting ground state), *every subsequent cycle
produces an exactly repeating, constant amount* of entropy production and
recorder mutual information per cycle, for both couplings tested, with
fidelity pinned at 1.000000 throughout. This directly operationalizes
condition (c)'s "renewable recorder" requirement: a tape of fresh ancillas
(not a fixed finite system) sustains nonzero A and R indefinitely while Θ
stays well-defined throughout. That specific requirement was prose in
`framework.md` v2.2 — it is now a concrete, numerically demonstrated
mechanism, grounded in the standard "collision model" literature
(Ciccarello, Lorenzo, Giovannetti & Palma, Phys. Rep. 2022).

**Round 4's error, caught by the round-5 adversarial code audit, and the
fix.** Round 4 claimed the swap coupling "commutes with `H_D`," making it
the natural test of condition (c)'s commutation clause, contrasted with a
non-commuting `σ_x⊗σ_x` coupling. **This claim was wrong.** Direct
computation of the commutator shows `[H_D, H_swap] ≠ 0` in general — swap
only commutes with the *total* free Hamiltonian `H_D+H_R`, and only because
this toy model set `ω_D=ω_R` (resonance). No coupling that exchanges
excitations between D and R can commute with `H_D` alone — that's a general
fact, not a parameter choice. So round 4's "commuting vs. non-commuting"
comparison actually tested "conserves total excitation number" vs. "doesn't
conserve anything," never the condition-(c) clause it claimed to test. The
audit also found both couplings preserved fidelity equally well at
`g=0.05`, which in hindsight was never going to distinguish anything, since
neither genuinely satisfied the condition being tested.

**Round 5 fix: add a coupling that actually commutes with `H_D` alone.**
`H_int = g·(σ_z⊗σ_x)` satisfies `[σ_z⊗I, σ_z⊗σ_x] = [σ_z,σ_z]⊗σ_x = 0`
identically, for *any* `ω_D, ω_R, g` — no resonance condition needed (verified
directly: `‖[H_D,H_zx]‖ = 0` to machine precision, vs. `‖[H_D,H_swap]‖ = 2.83`
and `‖[H_D,H_xx]‖ = 4.0` at `g=1`). A coupling-strength sweep
(`g ∈ [0.05, 4.0]`, `Γ0=1` fixed) then gives a clean, genuine test:

| g | zx (commutes with H_D) — min fidelity | swap (commutes with H_D+H_R only) | xx (commutes with neither) |
|---|---|---|---|
| 0.05 | 1.000000 | 1.000000 | 1.000000 |
| 0.5  | 1.000000 | 0.999781 | 0.998784 |
| 1.0  | 1.000000 | 0.999998 | 0.990577 |
| 2.0  | 1.000000 | 0.999999 | 0.969252 |
| 4.0  | 1.000000 | 0.999999 | 0.951672 |

`zx` stays *exactly* 1.000000 at every coupling strength tested, up to 4×
the bath relaxation rate — Θ's well-definedness is completely insensitive
to how strongly a modular-generator-commuting recorder is coupled. `xx`
degrades monotonically and substantially as coupling increases. This **is**
the genuine confirmation condition (c)'s original commutation clause needed
and round 4 failed to provide.

Re-running the full tape-recorder (`reset_period=8`, 25 cycles) at `g=2.0`,
where the contrast is clearest, gives three qualitatively different,
individually stable, repeating steady states:

| Coupling | Entropy produced / cycle | Mutual-info gained / cycle | Fidelity band (post-cycle-0) |
|---|---|---|---|
| zx (commutes with H_D) | 0.690394 nats | 0.000173 nats | exactly 1.000000, always |
| swap (commutes with H_D+H_R only) | 0.313193 nats | **0.000000** nats | 0.973698–1.000000 |
| xx (commutes with neither) | 3.453036 nats | 0.044425 nats | 0.960963–0.981480 (never returns to 1) |

Three genuinely new, honest findings here, none hypothesized going in:

1. **Condition (c)'s commutation clause is now confirmed, correctly
   tested**: a coupling that truly commutes with `H_D` keeps Θ perfectly
   well-defined regardless of coupling strength; one that doesn't,
   degrades it increasingly as coupling strengthens.
2. **`xx` never returns to fidelity 1** between resets at this coupling
   strength (floor ≈0.961, ceiling ≈0.981) — unlike the weak-coupling case,
   Θ is now only *approximately* defined throughout the whole renewable-tape
   process, a genuinely different (worse) regime than conditions (a)+(c)
   together were meant to describe.
3. **The swap coupling produces zero net mutual information gain per cycle**
   even though it produces substantial entropy (0.313 nats/cycle) — a
   renewable recorder can be *thermodynamically* active (dissipating) while
   being *informationally* inert (recording nothing new on net). This
   means condition (c) needs both a "renewable" clause *and* a clause
   ensuring the coupling actually transfers recoverable information, not
   just energy/entropy — `zx`, not `swap`, is the coupling that satisfies
   both simultaneously in this toy model.

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

1. Condition (c) now has a concrete, literature-grounded mechanism
   (renewable recorder / collision-model tape) **and**, after the round-5
   correction, a correctly-tested, confirmed commutation clause: a coupling
   that truly commutes with the clock's free Hamiltonian preserves Θ's
   well-definedness exactly, at any tested coupling strength; one that
   doesn't, degrades it increasingly with coupling strength. A third,
   independent requirement was also found and added: the coupling must
   transfer *recoverable information*, not just energy — a coupling can be
   renewable, commuting, and thermodynamically active while still recording
   nothing (the `swap` case, zero net mutual-information gain per cycle).
2. Condition (b2)'s proposed fix (diagonal Rényi invariants) is **neither
   confirmed nor refuted** by this round — it needs either a more faithful
   reconstruction of de la Hamette's "ideal frame" formalism or a different
   toy model, before `framework.md` can say anything stronger than "open."
3. The A/KMS structural tension flagged in round 3 was not just a worry —
   this round's base-case simulation (section 1 above) shows it actually
   happening, which is useful independent confirmation that round 3's
   holistic read caught something real rather than a hypothetical concern.

## Round 5 — adversarial code/physics audit, and what it changed

After round 4's results were written up, a fresh adversarial reviewer
audited the code and physics the same way earlier rounds audited prose
citations (see `self_critique.md`). It found: (a) a harmless-to-headline-
numbers but real regularization artifact at the exact initial pure state
(corrected above, §1), and (b) a genuine physics error — the claim that the
`swap` coupling "commutes with `H_D`" was false, meaning round 4's test of
condition (c)'s commutation clause never actually tested that property.
Rather than patch the claim and move on, the error was fixed at the source:
a coupling that genuinely commutes with `H_D` (`σ_z⊗σ_x`) was added, a
coupling-strength sweep was run to find where commuting vs. non-commuting
behavior actually diverges, and the tape-recorder test was rerun in that
regime (§2 above). The corrected result is *stronger* than round 4's
original (wrong) one: condition (c)'s commutation clause is now genuinely
confirmed, not just asserted past an untested comparison, and a third
requirement (informational, not just thermodynamic, activity) was
discovered in the process of fixing the error.

## Honest status

All three sub-goals from the `/goal` command now have a result. Condition
(c) is operationalized, correctly tested, and confirmed (three joint
requirements: renewable, commuting with the clock's generator, and
informationally active — demonstrated in a single coherent toy model).
Condition (b2)'s fix remains an honest "inconclusive" — not forced to an
answer either way, because the toy model's own fidelity to the cited
formalism couldn't be confirmed in the time available. The adversarial
code audit (round 5) caught a real error in round 4's reasoning and the fix
led to a cleaner, better-supported result than the original claim — the
same pattern this project's adversarial-review discipline produced on prose
in rounds 1–3, now shown to work on code and numerics too.
