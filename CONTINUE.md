# Continuing this research — start here with zero prior context

This file exists so that someone (human or AI agent) who clones this repo
fresh, with no memory of how it was built, can pick the work back up without
re-deriving what's already settled or repeating mistakes that were already
caught.

Read the files in this order:

```
1. CONTINUE.md       (this file — orientation, what to do next)
2. framework.md       (the actual research content — read in full, it's short)
3. self_critique.md   (the reasoning log — read if you want to know WHY
                        things are the way they are, or before changing
                        anything framework.md already settled)
```

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

In priority order, from `self_critique.md`'s round-3 conclusion:

### 1. Operationalize condition (c) — highest priority
`framework.md` §3, Claim 2 condition (c) currently says the recording
apparatus must "couple to the clock's modular Hamiltonian generator" in a
sense that's described in prose, not mathematics. A candidate fix is
sketched (commutator of the detector's interaction Hamiltonian with the
modular generator vanishing in some limit) but it has never been checked
against literature or written down precisely. This needs:
- A literature search specifically for "Unruh-DeWitt detector modular
  Hamiltonian coupling" and adjacent terms, done by someone (or an agent)
  who independently verifies anything they find rather than asserting it —
  see the citation-discipline note below.
- A precise mathematical statement, not a prose gesture.

### 2. Build an actual computable toy model — the real bottleneck
Nothing in this project has been computed yet. Every claim is literature
synthesis and logical argument, not a worked example. The recommended
starting point (from the round-1 novelty referee and round-3's structural
finding): an Unruh–DeWitt detector in a Rindler wedge, coupled to a separate
qubit "recorder," or a two-mode Gaussian thermal state — something where T,
A, R, Θ can each be computed in closed form as functions of a shared control
parameter.

**Known obstacle, found in round 3, that any attempt will hit first:** if
you naively put the detector/recorder in the same KMS/stationary state used
to define Θ, A will come out identically zero (stationary states have zero
average entropy production by construction — see the Kawai–Parrondo–Van den
Broeck relation cited in `framework.md` §3). You need the recorder to be a
genuinely separate, driven-out-of-equilibrium subsystem coupled to the
stationary reference, not the reference itself. This is exactly the physics
already studied in Erker et al. (PRX 7, 031022, 2017, "Autonomous quantum
clocks" — already cited in `framework.md`), which trades off a clock's
accuracy against the entropy it must dissipate. Start there.

**Also decide explicitly, before computing anything:** what reparametrization
class you're actually testing for. `framework.md` narrows this to "affine"
(matching the published Rovelli–Smerlak result) after round 1 found the
original "any monotonic reparametrization" claim was unsupported. Don't
silently drift back to the weaker claim — if your toy model only shows
monotonic (not affine) agreement, that's a weaker, different result, and
should be reported as such, not conflated with Claim 2 as currently stated.

### 3. Check de la Hamette's diagonal Rényi invariants as a fix for (b2)
Condition (b2) requires fixing not just a subsystem partition but also a
quantum reference frame (QRF), because mutual information and the modular
Hamiltonian both turn out to be frame-relative (round 1 finding — see
Giacomini, Castro-Ruiz & Brukner, Nat. Commun. 10, 494, 2019, and de la
Hamette, arXiv:2603.23598, 2026, both verified real in round 2). De la
Hamette's paper proposes *diagonal Rényi invariants* that stay bounded across
QRF changes even when raw entropy/mutual information don't. Nobody has
checked whether substituting these into R (and possibly Θ) actually rescues
condition (b2), or just moves the problem again. This is a concrete,
well-scoped next analytical step — read that paper and work it out.

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
