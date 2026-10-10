# Framework: When Do Geometric Duration, Entropic Time, and Quantum Information Agree?

Status: v2 (post round-1 adversarial review — 4 independent referees, see self_critique.md)
Owner: Ganesh Gupta | Started: 2026-10-10 | Revised: 2026-10-10

## 0. The question this document answers

Your original claim: the "time" in relativity (woven into spacetime, geometric,
gives proper time / dilation / length contraction) is a *different kind of thing*
from the "time" in thermodynamics (statistical, tied to entropy increase, the
irreversible arrow). **This is correct and is the standard view in physics.**
This document tries to state precisely how that notion, plus a third
(information-theoretic time: correlations, records, decoherence), relate —
and, after one round of adversarial review, how much of that precise statement
is actually new versus already published.

## 1. Three ontologically different "times" — stated precisely

| Notion | Formal object | Category | What changes it |
|---|---|---|---|
| Proper time τ | `dτ² = -ds²/c²` along a timelike worldline | **Geometric** (part of g_μν) | Mass-energy distribution, relative velocity, gravitational potential |
| Thermodynamic time | Direction of entropy increase, `dS/dt ≥ 0` | **Statistical / macroscopic** | Macrostate partition, initial low-entropy boundary condition |
| Informational time | Ordering from correlations/records (mutual information, Page–Wootters) | **Epistemic / relational** | Subsystem split, *and* choice of quantum reference frame (§4) |

**Claim 1 (established, verified, survives review):** Proper time is
worldline-indexed and partition-independent; thermodynamic/informational time
require choosing a system/environment split. Verified by adversarial review:
for `|ψ(τ)⟩ = cos(ωτ)|00⟩ + sin(ωτ)|11⟩`, `S(ρ_A) = H_bin(cos²ωτ)` oscillates
between 0 and `ln 2` with period `π/2ω` while `S_global ≡ 0` and proper time
advances monotonically throughout. Reviewer-added strengthening: a partition
aligned with a conserved quantity (or `H = H_A⊗I + I⊗H_B`) gives *constant*
subsystem entropy under the same global dynamics — so partition choice doesn't
just add noise, it can qualitatively flip the behavior (oscillating / constant
/ monotonically increasing), which is a sharper argument than a single example.

## 2. The three bridges that exist in the literature — corrected

### Bridge A — Unruh effect (geometric → statistical)
Proper acceleration `a` of a worldline → thermal bath at `T_U = ℏa/2πck_B` for
that observer (Unruh 1976). Rigorously derived in QFT; not yet directly
measured (achievable lab accelerations give unmeasurably small T_U).

### Bridge B — Jacobson (1995), corrected
Demanding the Clausius relation `δQ = T dS` hold across local Rindler horizons,
using `T_U` and an **area-law entropy** `S ∝ 𝒜_horizon` (Bekenstein–Hawking form —
`𝒜_horizon` for horizon area, kept visually distinct from §3's entropy-production
leg `A`, which is an unrelated quantity reusing a common symbol —
*not* "entanglement entropy," which is a later reinterpretation, see Bridge C),
reproduces the Einstein field equation as an equation of state
(Jacobson, gr-qc/9504004).

**Jacobson's own stated scope (missing from v1, added now):** in later
papers (gr-qc/0602001, gr-qc/0612078) Jacobson is explicit that the
derivation presupposes the spacetime manifold, metric, and local causal
structure, and derives only the *dynamical law* — exactly as the ideal-gas
law `pV = NkT` is derived from thermodynamics without deriving the existence
of molecules. Under this reading, "the derivation presupposes what it claims
to explain" is not a flaw, it's a declared scope limit. **This is the
rebuttal to the circularity objection in §4, and v1 omitted it entirely.**

### Bridge C — Entanglement entropy / Entanglement Equilibrium
Jacobson (2015, arXiv:1505.04753) and Casini et al. reinterpret the area-law
entropy as *entanglement* entropy of the vacuum across a causal diamond, and
show demanding it be stationary at its maximal value reproduces the
linearized Einstein equation. This is a genuinely separate, later argument
from Bridge B, not the same one dressed differently.

### Bridge C′ (the real prior art for Claim 2, found in round 1 — v1 missed this)
- **Martinetti & Rovelli**, "Diamond's temperature" (gr-qc/0212074) and
  **Menicucci, Olson & Milburn** (arXiv:1108.0883) already study exactly when
  thermal/modular time can be identified with proper time for bounded
  trajectories — this *is* the Θ↔T question, 15+ years before this draft.
- **Rovelli & Smerlak**, "Thermal time and the Tolman–Ehrenfest effect"
  (arXiv:1005.2985, CQG 2011) **already states the coincidence condition**:
  in a stationary spacetime with a timelike Killing flow, a KMS state's
  thermal/modular time Θ and proper time T are related by
  `k T_loc = ℏ dτ_thermal/dτ_proper` — i.e. they coincide **up to an affine,
  temperature-set rescaling**, precisely when the state is KMS and the flow
  is the Killing/Rindler flow. This is the published version of what v1's
  Claim 2 asserted as new for the T–Θ leg.
- **"The Time in Thermal Time"** (arXiv:2407.18948) and **Vidotto,
  "Thermodynamics without Time"** (arXiv:2409.19098) independently raise the
  circularity objection: the KMS condition needed to define "thermal"
  already presupposes a one-parameter automorphism group — i.e. thermal time
  needs time to get started. This reinforces, not contradicts, §4's
  circularity row.
- **Weberszpil & Sotolongo-Costa**, "Entropy as a Clock" (2026, already in
  the original literature pass but under-used) **already unifies three of
  the four legs**: entanglement-entropy growth (≈ A), KMS modular flow (≈ Θ),
  and Page–Wootters relational time (≈ R) into one framework with a derived
  parametrization `τ(ΔS) = (ΔS/λ)^(1/γ)`.
- **Höhn, Smith & Lock**, "The Trinity of Relational Quantum Dynamics"
  (arXiv:1912.00033) prove equivalence of Dirac-observable, Page–Wootters,
  and relational-Heisenberg clocks under stated conditions — the closest
  existing *methodological* precedent for "when do different time
  definitions coincide," though confined to the relational-clock family.
- **Erker, Mitchison, Silva, Woods, Brunner & Huber**, "Autonomous quantum
  clocks" (PRX 7, 031022, 2017) already trade off entropy-production rate
  (≈ A) against clock accuracy — an existing A-vs-clock-quality result.

**Revised novelty verdict for Claim 2: PARTIALLY ANSWERED, not a genuine gap.**
The T–Θ coincidence condition and the A–Θ–R unification both already exist,
separately, in the literature above. What does *not* yet exist (see §3) is
(i) treating T as a fourth, independently-varying leg rather than only
`Θ → T` in the Rindler/Killing special case, and (ii) an operationalized
version of condition (c) below.

## 3. The T / A / R / Θ operational split — revised

- **T** = `∫dτ` — geometric, partition-independent, frame-independent.
- **A** = `D_KL(P_F ‖ P_R^rev)` — the *ensemble-averaged* entropy production
  (Kawai–Parrondo–Van den Broeck, PRL 2007, `⟨σ⟩ = k_B D(ρ‖ρ̃)`), not the
  full fluctuating trajectory-level quantity constrained by the detailed
  fluctuation theorem. Partition- *and* frame-dependent (see below).
- **R** = `I(system:record)` — **not well-defined by a partition alone.**
  Round-1 finding (quantum information referee): per Giacomini,
  Castro-Ruiz & Brukner (Nat. Commun. 10, 494, 2019, arXiv:1712.07207) and
  de la Hamette (arXiv:2603.23598, 2026), mutual information for a *fixed*
  bipartition still depends on which subsystem's quantum reference frame
  (QRF) is used to describe the other. Two observers can agree on the
  partition and still compute different R. This is strictly worse than
  "partition-dependent" — it is **partition-and-frame-dependent**, and §4's
  v1 treatment of QRF relativity as a secondary bolt-on critique was wrong
  in degree, not just missing a citation.
- **Θ** = modular/thermal time parameter of a KMS state ρ.
  **Correction (v1 error, caught in round 1):** v1 claimed Θ was special
  because it is "derived from a state, not imposed," implying some immunity
  to the partition/frame problem above. This is false: the reduced state ρ
  used to build the modular Hamiltonian is itself obtained by tracing out a
  complement relative to a chosen QRF — the identical operation that makes R
  frame-relative. If ρ is frame-relative, Θ inherits that relativity. Θ has
  **no special immunity**; it was wrong to treat it as the one quantity that
  escapes the partition problem.

**Claim 2 (conjectural, unvalidated — no toy model exists yet; do not read
this as an established result the way Claim 1 is), revised and narrowed:**
T, A, R, and Θ coincide (up to an affine
reparametrization — not the unrestricted "monotonic reparametrization" v1
claimed; round-1 found no literature support for anything looser than affine,
and Rovelli–Smerlak's own result is affine) only when:

(a) the reduced state ρ_clock that defines Θ — i.e. the geometry/horizon
    degree of freedom whose modular flow gives the thermal-time parameter —
    is KMS/thermal. **Correction (round 3, holistic re-read):** this cannot
    also be the state A is evaluated on. A KMS/stationary state has, by
    construction, `A = D_KL(P_F‖P_R^rev) = 0` (forward and reverse path
    distributions coincide at equilibrium by definition of stationarity) —
    while T keeps advancing. A constant A cannot be affinely related to a
    monotonically advancing T; condition (a) as v2 stated it made A and T
    structurally incompatible in exactly the regime Claim 2 was narrowing
    toward. The fix: A and R must be evaluated on a **separate, locally
    coupled recording subsystem** that is driven *out* of equilibrium with
    ρ_clock (this is precisely the regime Erker et al., PRX 2017, already
    study — accurate autonomous clocks require nonzero entropy production in
    the readout device, even when read off a stationary reference). Condition
    (c) below must therefore constrain both A and R's apparatus, not R alone
    as v2 implied.
(b1) the partition matches the modular/Killing splitting (this is necessary
     but, per Bisognano–Wichmann, only pins down Θ for a *specific* worldline
     — its own proper acceleration sets the affine constant; "observers" in
     the plural, as v1 said, was imprecise),
(b2) **(new, split out from v1's single condition b)** the quantum reference
     frame used to define the reduced state ρ (and hence R and Θ) is also
     fixed and matches the frame implicit in picking out the worldline in
     (b1) — without this, (b1) alone does not guarantee agreement, per the
     QRF finding above. **Round 4 status: a candidate fix was tested and
     the test was inconclusive, not negative.** A minimal 3-qubit Z2 QRF
     toy model (`toy_model_qrf_invariant.py`) confirmed the underlying
     problem directly — a generic physical state gives genuinely different
     raw reduced-state entropies for the same subsystem depending on which
     of two candidate systems plays "the frame" — but the proposed fix (de
     la Hamette's diagonal Rényi invariant, arXiv:2603.23598, fetched and
     checked directly this round rather than taken on a prior reviewer's
     paraphrase) could not be confirmed to rescue it in this construction:
     neither raw nor dephased Rényi entropies matched across frames for a
     generic state. Most likely explanation: the simple conditional-flip
     toy construction used here does not satisfy the paper's formal "ideal
     frame" preconditions, not that the published theorem is wrong. Left
     open rather than forced to a conclusion either way — see `toy_model.md`
     §3 for the full reasoning and what would need to change to test this
     properly.
(c) the recording/readout apparatus (the non-equilibrium subsystem that
    actually produces nonzero A and a nonzero, legible R per the (a)
    correction above) must be a **renewable** degree of freedom — a
    "tape" of fresh ancillas, not a single fixed finite system — coupled to
    the clock's modular Hamiltonian generator.
    **Round 4 (2026-10-10): this is no longer pure prose.** A computable toy
    model (`toy_model.md`, `toy_model_detector_recorder.py`,
    `toy_model_tape_recorder.py`) confirmed the structural worry in (a)
    numerically — a *static* recorder's mutual information with the clock,
    and the joint entropy production, both decay toward zero at late proper
    time even though the clock reaches its KMS/Gibbs state almost
    immediately — and then showed that periodically refreshing the recorder
    (a standard "collision model" / repeated-interaction construction;
    Ciccarello, Lorenzo, Giovannetti & Palma, Phys. Rep. 954, 1–70 (2022),
    arXiv:2106.11974) fixes it: after one transient cycle, every subsequent
    cycle produces an *exactly repeating*, nonzero entropy-production and
    mutual-information gain, while the clock's fidelity to its Gibbs state
    stays pinned at 1.0 throughout (i.e. Θ stays well-defined the whole
    time). **Round 5 correction and completion:** round 4's first attempt to
    test the commutation clause used a coupling (`swap`) it incorrectly
    claimed "commutes with H_D" — an adversarial code audit caught this (it
    only commutes with `H_D+H_R`, and only at resonance; no exchange
    coupling can commute with `H_D` alone). Fixed by adding a coupling that
    genuinely does (`σ_z⊗σ_x`, commutes with `H_D` identically for any
    parameters) and sweeping coupling strength: the genuinely-commuting
    coupling keeps the clock's fidelity to its KMS state at exactly 1.0 at
    every tested strength (up to 4× the bath rate); a genuinely
    non-commuting coupling (`σ_x⊗σ_x`) degrades it increasingly and
    persistently as coupling strengthens. **Condition (c)'s commutation
    clause is now correctly tested and confirmed**, not merely asserted.
    A third, independent requirement also emerged from the corrected run:
    the coupling must transfer *recoverable information*, not just
    energy/entropy — the `swap` coupling (commutes with `H_D+H_R` only) is
    renewable and thermodynamically active (0.31 nats entropy/cycle) but
    records *zero* net mutual information per cycle. Condition (c) is
    therefore: the apparatus must be (i) renewable/tape-like, (ii) coupled
    in a way that commutes with the clock's own free Hamiltonian (not just
    the total Hamiltonian), and (iii) coupled in a way that actually
    transfers recoverable correlation, not only energy — all three now
    numerically confirmed together in one toy model (`toy_model.md` §2).

**What remains actually novel after round 1:** not the existence of a
coincidence condition (published, see Bridge C′), but (i) making condition
(b2) explicit as independent from (b1) — no source found treats partition-
fixing and frame-fixing as separate requirements for this specific
comparison — and (ii) operationalizing (c). Both are modest, not
revolutionary, contributions, and neither is validated yet; they are
candidate next steps, not results.

## 4. Known critiques — corrected citation table

| Critique | Status after round 1 | Correct source |
|---|---|---|
| Circularity: Jacobson-style derivations presuppose local Lorentz invariance/causal structure | **Real objection, but has a standing rebuttal v1 omitted** (Jacobson: derives only the equation of state, not spacetime itself — gr-qc/0602001, gr-qc/0612078) | v1 cited "Chua & Callender (2025, arXiv:2507.10529)" for this — **confirmed wrong**, that paper is about the Tolman effect/temperature in GR, not this circularity argument. Citation removed. |
| Empirical tension with entropic gravity | Real but contested, and scope-limited to Verlinde specifically | Kobakhidze, arXiv:1108.4161 (hep-th preprint — v1 wrongly said "Phys.Rev.D"; also combines neutron interferometry *and* GRANIT bouncing-ultracold-neutron data, not "neutron interferometry" alone). **Disputed** by Chaichian, Oksanen & Tureanu (arXiv:1104.4650, 1109.2794), who argue Kobakhidze oversimplified Verlinde's formalism and that entropic gravity reduces to Newtonian gravity in the tested regime, i.e. no real conflict. v1 presented this as a settled refutation; it is a live exchange. Scope-limit claim itself (doesn't touch Jacobson/Unruh/Rovelli) is accurate. |
| Partition circularity (can't define entanglement/subsystems if space emerges from entanglement) | Real philosophical point, **misattributed in v1** | v1 cited "Al-Khalili & Chen (2024)" — **confirmed wrong**; their actual 2024 paper (arXiv:2405.03418) proposes an Entanglement Past Hypothesis and never makes this argument. This error originated in the source literature review this project started from and was propagated into v1 without independent verification — logged as the primary process mistake in self_critique.md round 1. No correct attribution found for this specific argument in round-1 searches; treat it as an unattributed but philosophically sound point (quantum-mereology literature, e.g. Carroll & Singh, is adjacent but not confirmed to make this exact claim) until verified further. |
| Does the Rindler/worldline route in (b1) escape partition circularity? (→ directly bears on Claim 2 condition b1, §3) | **No — confirmed by two independent reviewers.** Defining a worldline's proper acceleration and its causal horizon already requires the full Lorentzian causal structure, not just a spatial split. This relocates the circularity rather than resolving it, and is only defensible under Jacobson's own weaker "equation of state given spacetime" reading (see Bridge B). v1's framing of this as an open "escape route... must verify" is replaced with a direct negative finding. |
| Thermal Time Hypothesis: modular flow is state-dependent, not structural | Accurate in substance, **mis-sourced in v1** ("Kuchař-style") | Correct source: Noel Swanson, "Can Quantum Thermodynamics Save Time?" (*Philosophy of Science* 88(2):281–302, 2021 — verified, round 2). Swanson's own four stated objections: implementing TTH in the classical limit; the thermal-time-vs-proper-time relationship; interpreting time flow in non-equilibrium states; lack of *gauge invariance* (not "background-independence" — corrected, round 2). The separate "KMS-needs-time" circularity point stays attributed only to Chua's "The Time in Thermal Time" (arXiv:2407.18948, Bridge C′ above) — round 2 found v1/v2 had double-counted it under Swanson's name as well, which his paper does not argue. |
| Quantum reference frame relativity | **Underweighted in v1** — treated as a bolt-on to R/A; actually also compromises Θ (see §3) and is not resolved merely by fixing a partition | Giacomini, Castro-Ruiz & Brukner, Nat. Commun. 10, 494 (2019); de la Hamette, arXiv:2603.23598 (2026); Valente, Ferradini, Giacomini & Kabel (ECAP 2026, in progress). De la Hamette's diagonal Rényi invariants are bounded under QRF changes even when raw entropy/mutual information are not — a possible escape hatch not yet incorporated into Claim 2 (candidate for round 2). |

## 5. What this framework does NOT claim (unchanged from v1, strengthened)

- It does not claim entropy causes gravity, or that time is "made of" information.
- It does not claim Θ is a complete or frame-invariant replacement for proper
  time; it coincides with proper time, *at best*, in the KMS/Killing special
  case, via an affine rescaling, for a specific worldline, in a specific QRF.
- It does not resolve the cosmological Past Hypothesis.
- **New, following the philosophy-of-physics review:** even the Jacobson/Casini
  "bridges" (Bridge B, C) remain, per the field's own philosophers
  (Wallace 2009; Dougherty & Callender's "Black Hole Thermodynamics: More
  Than an Analogy?"), **contested as to whether they describe a literal
  physical mechanism or a robust formal analogy** (matching equation *form*
  between the Clausius relation and the Einstein equation is not by itself
  evidence of a shared physical mechanism). v1's §2 called these "three
  narrower, real bridges" before any critique appeared — that framing was
  more confident than the field's actual treatment and is corrected here:
  they are *real, derived results*, whose *interpretation* as literal
  thermodynamic mechanisms (vs. formal analogy) is unsettled.
- Verlinde's specific entropic-gravity program is widely regarded in
  mainstream GR circles as disfavored following the empirical and internal
  critiques (§4); this framework's Bridges A/B/C/C′ do not depend on
  Verlinde's program and are unaffected by its disfavor.

## 7. Computational layer (round 4, new)

As of v2.2, every claim above was literature synthesis and logical argument
— nothing had been computed. Round 4 built and ran three toy models to test
Claim 2's conditions directly rather than only argue about them:

```
toy_model_detector_recorder.py   — base case: static recorder, confirms the
                                     round-3 A/KMS structural tension really
                                     happens numerically
toy_model_tape_recorder.py       — fix: periodically-refreshed recorder,
                                     operationalizes condition (c)
toy_model_qrf_invariant.py       — test of a proposed fix for condition
                                     (b2); result: inconclusive, not negative
```

Full writeup, honest about what worked and what didn't, in `toy_model.md`.
Headline results: condition (c) now has a working, numerically-demonstrated
mechanism (a renewable recorder, grounded in standard collision-model
physics) though one sub-clause (commutation with the modular generator)
remains untested at the parameters tried; condition (b2)'s proposed fix
remains genuinely open, reported as such rather than forced to an answer.

## 6. Status log

- v3.1 (2026-10-10): round 5 — adversarial code/physics audit of round 4's
  toy models (same discipline applied to code that rounds 1–3 applied to
  prose). Found a regularization artifact (harmless to headline numbers,
  fixed/caveated) and a genuine physics error (round 4's claimed
  "commuting" coupling didn't actually commute with the clock's Hamiltonian
  alone, so condition (c)'s commutation clause was never properly tested).
  Fixed by adding a genuinely-commuting coupling and a coupling-strength
  sweep: condition (c) is now correctly tested and confirmed, with a third
  requirement (informational activity, not just renewability and
  commutation) discovered in the process of fixing the error. See
  `toy_model.md` §2 and round 5 of `self_critique.md`.
- v3 (2026-10-10): round 4 — first computational round. See §7. Condition
  (c) operationalized; condition (b2)'s candidate fix tested and found
  inconclusive (toy construction likely doesn't satisfy the cited theorem's
  preconditions, not evidence against the theorem itself). No claims were
  weakened or invalidated this round; two were sharpened from prose to
  checkable code.
- v2.2 (2026-10-10): round-3 holistic whole-document adversarial pass (after
  two narrow-slice rounds + a citation check) found one real structural gap
  missed by every narrow referee: condition (a) as stated made A (entropy
  production) and T (proper time) structurally incompatible, since a
  KMS/stationary state has `A ≡ 0` by construction while T keeps advancing.
  Fixed by splitting "the KMS state that defines Θ" from "the non-equilibrium
  recording subsystem that defines A and R," and folding both into condition
  (c). Also fixed: a symbol collision (horizon area vs. the A leg), added an
  explicit conjectural/unvalidated tag directly on Claim 2's header, and
  cross-referenced the (b1)-circularity finding from Claim 2 itself. No
  fatal flaw found in this round — this is the convergence signal the
  self-critique log uses to stop the adversarial loop (see self_critique.md
  round 3).
- v2.1 (2026-10-10): round-2 citation-verification pass checked all 10 new
  sources introduced in v2 against primary sources. 9/10 confirmed exactly
  as cited; 1 (Swanson) had a minor venue-date error and a double-attributed
  sub-claim, fixed above. No fabricated or reversed citations found this
  round — unlike round 1, which found two.
- v1 (2026-10-10): initial draft. Claim 1 established, Claim 2 proposed as a
  new conjecture, critiques collected but unverified.
- v2.1 (2026-10-10): round-2 citation-verification pass checked all 10 new
  sources introduced in v2 against primary sources. 9/10 confirmed exactly
  as cited; 1 (Swanson) had a minor venue-date error and a double-attributed
  sub-claim, fixed above. No fabricated or reversed citations found this
  round — unlike round 1, which found two.
- v2 (2026-10-10): post round-1 adversarial review (4 independent referees:
  GR/QG, quantum information, philosophy-of-physics + empirical fact-check,
  novelty/publication-bar). Found: 2 misattributed/wrong citations removed,
  1 miscited venue + omitted rebuttal fixed, 1 missing standard rebuttal
  added (Jacobson's own scope statement), Claim 2 downgraded from "genuine
  gap" to "partially answered" with the actual residual-novel content
  isolated (condition b2, condition c), Θ's claimed immunity to QRF
  relativity retracted, reparametrization class narrowed from "monotonic" to
  "affine" (matching the actually-published Rovelli–Smerlak result).
  **Next action:** verify the *new* citations introduced in this revision
  (Rovelli–Smerlak, Martinetti–Rovelli, Menicucci-Olson-Milburn, Höhn-Smith-
  Lock, Erker et al., Swanson, Kawai-Parrondo-Van den Broeck, de la Hamette,
  Dougherty & Callender, Chaichian-Oksanen-Tureanu) before treating them as
  reliable — round-1 proved subagent-reported citations are not
  self-certifying.
