# Continuing this research — start here with zero prior context

This file exists so that someone (human or AI agent) who clones this repo
fresh, with no memory of how it was built, can pick the work back up without
re-deriving what's already settled or repeating mistakes that were already
caught.

Read the files in this order:

```
1. CONTINUE.md        (this file — orientation, what to do next)
2. framework.md        (the actual research content — read in full, it's short)
3. toy_model.md         (round 4: what was actually computed, and found)
4. self_critique.md    (the reasoning log — read if you want to know WHY
                         things are the way they are, or before changing
                         anything framework.md already settled)
5. BIBLIOGRAPHY.md     (every source, in the order it entered the reasoning,
                         with verification status)
```

The three `toy_model_*.py` scripts are runnable (`python3 toy_model_*.py`,
numpy/scipy only, no QuTiP) and regenerate every number in `toy_model.md`
from scratch in under a minute.

## What this project is

A single, narrow research question: when you talk about "time" in physics,
you're actually conflating at least three different things —

1. **Proper time** (relativity): geometric, part of the metric, defined per
   worldline, needs no observer choices.
2. **Thermodynamic time**: the entropy-increase arrow, a statistical property
   of a chosen system/environment split, not of the universe as a whole.
3. **Informational time**: orderings built from quantum correlations, records,
   and decoherence — depends on partition *and* on which quantum reference
   frame is doing the describing.

The project's output is `framework.md`: a precise statement of how these
three relate, which parts are established physics (Claim 1 — yes, these are
genuinely different, this is standard and verified), and which part is a
narrow, mostly-already-published, partially-novel conjecture (Claim 2 — a
four-quantity coincidence condition: proper time T, entropy production A,
recorded information R, and modular/thermal time Θ).

## What's already done — do not redo this

- Claim 1 is established and verified (two-qubit counterexample checked by
  hand and by an adversarial reviewer). Treat it as solid ground.
- Claim 2 has been through **three full rounds of independent adversarial
  review**: (1) four specialist referees — GR/quantum gravity, quantum
  information, philosophy-of-physics + empirical fact-check, novelty/
  publication-bar; (2) a dedicated citation-verification pass on every new
  source introduced in round 1; (3) a holistic whole-document read checking
  for anything the narrow specialists missed. Current version is v2.2.
- The adversarial loop found and fixed real errors along the way: two
  misattributed citations (one of which was inherited from the original
  literature review this project started from — **lesson: never trust a
  citation, even one in a document you're building on, without checking the
  actual paper**), a false claim that one quantity (Θ) was immune to
  observer-dependence (it isn't), an overclaimed equivalence class (claimed
  "any monotonic reparametrization," literature only supports "affine"), and
  a genuine internal inconsistency introduced by an earlier fix (entropy
  production A is identically zero exactly where an earlier condition
  required it to be meaningfully nonzero — fixed by separating "the clock"
  from "the recorder" as two different physical subsystems).
- `self_critique.md` has the full reasoning trail for every one of those.
  If you're about to second-guess something in `framework.md`, check there
  first — the reasoning for why it's stated the way it is (and what was
  tried and rejected) is probably already written down.

## What's NOT done — this is the actual to-do list

Round 4 (2026-10-10) did real computation for the first time — see
`toy_model.md`. Two of the three items below are now partially done with
numerical results; none are fully closed. In priority order:

### 1. DONE — condition (c) fully operationalized and confirmed (round 5)
Round 4 attempted to test the commutation clause with a coupling it
wrongly claimed "commutes with H_D" (it only commutes with H_D+H_R, at
resonance). A round-5 adversarial code audit caught this; the fix (a
genuinely-commuting `σ_z⊗σ_x` coupling, verified `[H_D,H_int]=0` by direct
computation, plus a coupling-strength sweep up to `g=4·Γ0`) confirmed the
commutation clause for real, and surfaced a third requirement nobody had
hypothesized: the coupling must also transfer *recoverable information*,
not just entropy (the `swap` coupling, renewable and thermodynamically
active, records zero net mutual information per cycle at strong coupling).
Condition (c) is now: renewable + commutes with the clock's own free
Hamiltonian + informationally active — all three confirmed together in one
toy model. See `toy_model.md` §2 and `self_critique.md` round 5. One loose
thread: *why* the swap coupling specifically records zero net information
at strong coupling was not explained, just observed — worth understanding
if this line of work continues.

### 2. Reconstruct the QRF "ideal frame" formalism more faithfully — the real bottleneck now
`toy_model_qrf_invariant.py` tested de la Hamette's diagonal-Rényi-invariant
fix (arXiv:2603.23598, formula fetched and verified directly — see
`BIBLIOGRAPHY.md` Stage 5) against a self-built 3-qubit Z2 QRF toy model,
and got a genuine **inconclusive** result: for a generic physical state,
neither the raw nor the dephased Rényi entropies of the target qubit
matched across the two candidate reference frames, which shouldn't happen
if the construction were a valid "ideal frame" in the paper's technical
sense. The most likely explanation (not yet confirmed) is that the simple
conditional-bit-flip frame-change map used here doesn't satisfy whatever
structural requirement "ideal frame" actually imposes (candidate guess: the
frame may need to carry a *faithful regular representation* of the symmetry
group, which a bare qubit might not for larger/different groups — but this
project's own Z2 case uses a qubit frame specifically because Z2 only has 2
elements, so even this guess needs checking against the paper's actual
definition of "ideal frame," not just its theorem statement). **Next step:
fetch and read de la Hamette's full definition of "ideal frame" (not just
Theorem 1), check whether the toy model's `frame_change_unitary` actually
qualifies, and fix the construction (or determine it can't be fixed for a
single qubit frame) before concluding anything about whether the fix itself
works.**

### 3. Verify the toy-model code and physics independently
A round-4 adversarial code/physics audit was dispatched (same discipline
used on every prose claim in rounds 1–3) — check `self_critique.md`'s most
recent round for its outcome before trusting any number in `toy_model.md`
at face value. If that audit found something, fix it and re-run before
building further on these results.

### 4. Decide the reparametrization class before computing further
`framework.md` narrows Claim 2's coincidence claim to "affine" reparametrization
(matching the published Rovelli–Smerlak result), not the weaker "monotonic"
v1 originally claimed. The round-4 toy models didn't yet test this
specifically (they showed Θ well-defined and A/R sustained, but didn't check
the precise functional relationship between Θ and T once both are
nontrivial). Any future toy-model work should check this explicitly, not
silently assume whichever relationship comes out.

## Standing discipline — apply this to any further work, don't skip it

This project's single most important process lesson, learned the hard way
across three adversarial rounds, is in `self_critique.md`'s "meta-lesson"
and round-3 entries:

- **Never let a citation — yours, a prior document's, or a reviewer
  agent's — enter `framework.md` as a flat assertion without independent
  verification.** Two real citation errors made it into v1 this way. If you
  (or an agent) add a new claim-with-citation, verify it against the actual
  paper before writing it down as fact, or mark it explicitly as unverified.
- **After any local fix, re-check the whole claim it belongs to, not just
  the objection that prompted the fix.** The round-3 finding (A and the KMS
  condition contradicting each other) existed because a round-1 fix, made to
  satisfy one specialist referee, silently broke compatibility with a
  different part of the same claim. Narrow, single-issue reviews will not
  catch this class of error — only a holistic re-read will.
- If you resume the adversarial-review loop (recommended before any attempt
  to make this a submittable paper), the pattern used successfully here was:
  draft/revise → dispatch several independent fresh reviewers in parallel,
  each with a narrow mandate and instructed to use live web search rather
  than recalled knowledge → fix what they find → dispatch a dedicated
  citation-verification pass on anything new they cited → dispatch one final
  holistic whole-document pass → log every round's connections, mistakes,
  corrections, and open objections in `self_critique.md` before declaring
  convergence. Stop when a round finds no new substantive defects, not when
  it finds literally zero issues (that bar is unrealistic for a document
  citing ~25 sources).

## Honest status, stated plainly

This is a well-cited, internally-consistent, adversarially-tested **research
proposal**. It is not a validated physical result, not new physics, and not
a submittable paper as-is — it has no computed example anywhere in it.
Anyone continuing this work (including a future instance of an AI agent)
should preserve that framing and not represent it as more settled than it
is, in this file or in `framework.md`.
