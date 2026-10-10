# Self-Critique & Meta-Learning Log

Purpose: track connections found, mistakes made and corrected, and cross-idea
links, across every round of adversarial review of `framework.md`. This file
is the agent's own error ledger for this investigation — not a summary of the
physics, a summary of how the reasoning process behaved.

## How to read this file

Each round gets one entry with four parts:
- **Connections found** — genuine links between previously separate ideas.
- **Mistakes caught** — claims in the framework that were wrong, overstated,
  or already refuted in the literature.
- **Corrections applied** — what changed in `framework.md` as a result.
- **Open objections** — things flagged but not yet resolved; carried to next round.

---

## Round 0 (2026-10-10) — initial draft, self-review before external adversarial pass

**Connections found:**
- Jacobson (1995) was missing from the user-supplied literature review despite
  being the historical origin of "gravity from thermodynamics" reasoning,
  15 years before Verlinde (2010). Mistake-of-omission in the *source material*,
  not mine — worth flagging since it changes the novelty assessment of Gap 4
  in the original review (the cosmological-boundary-condition gap looks more
  mature once Jacobson + Casini/entanglement-equilibrium lineage is included).
- Rovelli–Connes Thermal Time Hypothesis, mentioned only in passing in the
  source material's comparison table, is actually the closest existing
  candidate to "time emerging from information" and deserves to be a load-
  bearing piece, not a footnote. Connected it to Unruh (Bridge A) via the
  fact that Rindler-wedge modular flow literally *is* geometric boost — this
  is a real, checkable mathematical fact (Bisognano–Wichmann theorem), not
  an analogy. This is the strongest finding of round 0.
- Bekenstein–Hawking black hole entropy was completely absent from the
  pasted literature review, which is a significant gap for a review spanning
  entropy + information + spacetime. Not yet incorporated into framework.md —
  carry to round 1 (does it strengthen or complicate Claim 2?).

**Mistakes caught (self-caught before external review):**
- First draft of Claim 2 did not restrict Θ to KMS states and implied it was
  a general-purpose clock. Caught by re-reading the Thermal-Time-Hypothesis
  critique (modular flow is state-dependent) before external review even
  started. Corrected in-place in v1 — logging it here anyway so the pattern
  ("generalize a result past the conditions under which it was proven") is
  visible for future rounds.

**Corrections applied:**
- Restricted Claim 2's Θ to the KMS/Rindler special case explicitly, with
  the Bisognano–Wichmann fact as the justification for why Θ = T there.

**Open objections (unresolved, carried forward):**
1. Circularity objection (Wald-style) against Jacobson/Casini bridges — does
   Claim 2 survive it, or does it just inherit the same circularity?
2. Al-Khalili & Chen partition-circularity objection — does the Rindler
   splitting (defined by a worldline, not by pre-existing space) actually
   dodge this, or is that an illusion?
3. Kobakhidze empirical refutation — confirm it only targets the Verlinde
   branch and does not touch Jacobson/Unruh/Rovelli, since the framework
   currently assumes this scope separation without having checked it.
4. QRF (Giacomini et al.) frame-relativity of "system"/"clock"/"record" —
   not yet modeled in Claim 2 at all; could be a bigger hole than the other
   three.
5. **Meta-level risk**: this entire framework was built by one continuous
   reasoning process (me) extending a document that was itself produced by
   an AI research-assistant persona. Self-consistency is not independent
   validation. This is exactly why external adversarial agents (not forks
   sharing this context) are being used for round 1, starting now.

**Next action:** dispatch independent adversarial reviewers (separate context,
no visibility into this reasoning) against framework.md v1, one per objection
above plus a general-rigor pass, with instructions to search for real
publications that already settle or sharpen each point.

---

## Round 1 (2026-10-10) — four independent adversarial referees vs. framework.md v1

Four fresh general-purpose agents, each with zero visibility into this log or
my reasoning, each given only framework.md v1 plus a distinct adversarial
mandate (GR/QG, quantum information, philosophy-of-physics + empirical fact-
check, novelty/publication-bar), each required to use live web search rather
than recalled knowledge.

**Connections found:**
- Rovelli & Smerlak (arXiv:1005.2985, CQG 2011) already states the exact T–Θ
  coincidence condition (KMS state, Killing flow, affine rescaling by local
  temperature) that v1's Claim 2 proposed as new. Links to [[framework]] §2
  Bridge C′.
- Weberszpil & Sotolongo-Costa (2026) — present in the *original* pasted
  literature review but under-used by me — already unifies three of the four
  legs (A, Θ, R) I was treating as separately novel. I had the citation in
  hand from the start and failed to connect it to my own Claim 2; this is a
  "didn't use what I already had" failure, distinct from a sourcing failure.
- Höhn, Smith & Lock's "Trinity of Relational Quantum Dynamics"
  (arXiv:1912.00033) is the closest methodological precedent for "prove
  several time-definitions coincide under stated conditions" — useful as a
  template for how to eventually state Claim 2 rigorously (equivalence
  theorem with explicit hypotheses), not just as a prior-art hit.
- The QRF-relativity objection (Giacomini–Castro-Ruiz–Brukner 2019,
  de la Hamette 2026) connects to Θ in a way I had not seen: Θ is built from
  a reduced state ρ, and ρ is only well-defined relative to a QRF — so the
  same frame-relativity that breaks R also breaks Θ. I had written Θ into
  v1 as the one quantity immune to the partition problem. It isn't. This
  single connection invalidates a structural claim in v1, not just a detail.

**Mistakes caught (this is the important part of this round):**
1. **Inherited, unverified citation**: v1's §4 attributed a "partition
   circularity" argument to Al-Khalili & Chen (2024). That attribution
   traces back to the *pasted literature review the user provided at the
   start of this conversation* — I copied its claim about that paper into
   framework.md without independently checking the actual paper. Two
   independent round-1 referees checked the real 2024 Al-Khalili & Chen
   paper (arXiv:2405.03418) and found it argues something else entirely
   (an Entanglement Past Hypothesis), not the circularity point attributed
   to it. **Lesson: a claim doesn't become trustworthy by surviving one
   layer of AI-generated synthesis. Every citation I did not personally
   verify should have been flagged as unverified in v1 rather than stated
   as fact.** This is the single most important process mistake of this
   project so far.
2. **Self-introduced wrong citation**: I cited "Chua & Callender (2025,
   arXiv:2507.10529)" as explicit support for the Jacobson-circularity
   objection. It is a real paper but is about the Tolman effect, not this
   argument — I pattern-matched a plausible-sounding citation from the
   pasted review's reference list onto a claim it doesn't actually support.
   Same lesson as (1), but this one I generated myself rather than inheriting.
3. **Overclaimed immunity**: I asserted Θ was special/immune to the
   partition-dependence problem because it is "derived from a state, not
   imposed." This is false reasoning — I mistook "derived from internal
   structure" for "frame-invariant," which do not imply each other. Caught
   by the quantum-information referee, not by my own round-0 self-review,
   which means my self-review (round 0) was not sufficient on its own —
   external adversarial review found a structural error my own re-reading
   missed entirely.
4. **Overclaimed reparametrization class**: v1 said T/A/R/Θ could coincide
   "up to monotonic reparametrization" with no justification for why
   monotonic (a very weak, easy-to-satisfy condition) rather than something
   stricter. The actual published result (Rovelli–Smerlak) only supports
   *affine* reparametrization. Weakening the claimed equivalence class to
   whatever makes it easiest to defend, without checking what the evidence
   actually supports, is a generalization-past-the-evidence pattern — same
   family of mistake as round 0's premature KMS generalization, but this
   time it survived into v1 because round-0 self-review didn't catch it.
5. **Wrong citation venue + omitted rebuttal**: Kobakhidze's paper was cited
   as "Phys.Rev.D" (likely remains an arXiv preprint) and presented as a
   clean empirical refutation of entropic gravity, omitting that Chaichian,
   Oksanen & Tureanu directly disputed it. Presenting a contested exchange
   as a settled result is an accuracy failure distinct from a wrong
   citation — it's an asymmetric-evidence failure (only searching for the
   claim, not for rebuttals to the claim).
6. **Wrong attribution for a correct idea**: the Thermal Time Hypothesis
   critique in v1 was substantively right but sourced to "Kuchař-style
   critiques," a vague gesture at a real person's real but different body of
   work (canonical quantum gravity's problem of time generally), rather than
   the actual source (Swanson 2018/2020). A plausible-sounding name is not a
   citation.

**Corrections applied (all in framework.md v2):**
- Removed the Chua & Callender citation from the circularity row; added
  Jacobson's own stated scope limitation (gr-qc/0602001, gr-qc/0612078) as
  the actual rebuttal, which v1 had omitted entirely rather than gotten wrong.
- Flagged the Al-Khalili & Chen attribution as unverified/likely wrong rather
  than repeating it as fact; left the underlying philosophical point
  standing but unattributed pending further search.
- Fixed Kobakhidze's venue, description (neutron interferometry *and*
  GRANIT ultracold-neutron data, not just interferometry), and added the
  Chaichian–Oksanen–Tureanu rebuttal so the critique reads as a live
  exchange, not a settled fact.
- Re-sourced the Thermal Time Hypothesis critique to Swanson, and added three
  further standard objections v1 was missing (KMS-needs-time circularity,
  equilibrium-only domain, lack of background-independence).
- Retracted Θ's claimed immunity to partition/frame relativity; split
  condition (b) into (b1) partition-fixed and (b2) frame-fixed, since they
  are independent requirements.
- Narrowed the reparametrization class from "monotonic" to "affine,"
  matching what Rovelli–Smerlak actually establishes.
- Reclassified Claim 2 from "genuine gap" to "partially answered," and
  explicitly isolated the two pieces that survive as actually-residual-novel
  (condition b2 stated as independent from b1; operationalizing condition c)
  rather than continuing to present the whole four-quantity coincidence idea
  as new.
- Softened §2's "three narrower, real bridges" framing and added the
  Dougherty & Callender "mechanism vs. analogy" caveat, per the philosophy
  referee's finding that v1 read as more settled than the field's actual
  treatment of Jacobson/Casini-style results.

**Open objections (carried to round 2):**
1. Every *new* citation introduced in this round's corrections (Rovelli–
   Smerlak, Martinetti–Rovelli, Menicucci-Olson-Milburn, Höhn-Smith-Lock,
   Erker et al., Swanson, Kawai-Parrondo-Van den Broeck, de la Hamette,
   Dougherty & Callender, Chaichian-Oksanen-Tureanu) was reported by a
   subagent and has NOT been independently re-verified by a separate check.
   Given mistake (1) above, treating subagent output as self-certifying
   would repeat the exact failure this round just caught. This is the
   required next action, not optional.
2. Condition (c) (recorder couples to the modular Hamiltonian's generator)
   remains unoperationalized; the candidate fix proposed in v2 (interaction
   Hamiltonian commutes with the modular generator up to a stated limit) is
   my own suggestion, untested against literature or a worked example.
3. No concrete computable toy model exists yet (novelty referee's main ask).
   Without one, Claim 2 stays a conjecture, not a checkable result, regardless
   of how carefully the citations are fixed.
4. De la Hamette's diagonal Rényi invariants were flagged as a possible
   escape hatch from QRF-relativity for R (and maybe Θ) but this has not
   been attempted or checked for whether it actually rescues condition (b2).

**Meta-lesson for this project going forward:** the single highest-value
discipline is to never let a subagent's (or a prior document's) citation
enter framework.md as a flat assertion. Every citation gets one of three
tags until independently checked: VERIFIED (I or a dedicated verification
pass confirmed the paper says this), REPORTED (a reviewer said so, not yet
checked), or RETRACTED (checked and found wrong). v2 does not yet carry
these tags explicitly in-line — add them in the next pass.

---

## Round 2 (2026-10-10) — dedicated citation-verification pass on all 10 new v2 sources

A fifth fresh agent, with no visibility into prior reasoning, was given only
the task of checking each of the 10 citations introduced during round 1's
corrections against primary sources (arXiv abstracts/full text, journal
records), explicitly warned that round 1 had already found two fabricated/
misattributed citations and told not to assume any of these are real just
because they sound plausible.

**Connections found:**
- De la Hamette's arXiv ID (2603.23598) initially *looked* like it could be
  fabricated (unfamiliar YYMM prefix), and the verifier flagged this
  explicitly before checking rather than assuming it was fine — this is
  exactly the right instinct, and it turned out to be a false alarm because
  today's date (2026-10-10) makes a March-2026 preprint chronologically
  normal. Worth recording as a reusable check: don't reject a citation on a
  surface-level "looks unusual" heuristic without verifying against the
  current date — the mistake there would have been false-negative paranoia,
  the mirror image of round 1's false-positive trust.

**Mistakes caught:**
- Swanson's cited critique bundle in framework.md v2 double-counted the
  "KMS-needs-time" circularity argument under both Swanson's name and
  Chua's "Time in Thermal Time" — Swanson's actual four objections (per his
  abstract) are about the classical limit, the thermal/proper-time
  relationship, non-equilibrium states, and gauge invariance, not KMS
  circularity. Also the venue/date ("2018/2020") was imprecise; actual
  publication is *Philosophy of Science* 88(2), 2021.
- No new fabricated citations were found this round. This is a meaningful
  data point, not just an absence of bad news: it suggests the round-1
  fabrications were not a generic failure mode of "subagents hallucinate
  citations routinely," but specifically a failure of **unverified reuse** —
  both round-1 errors were citations asserted without a dedicated
  verification step, whereas these 10 were generated *as findings from a
  live, cited web search* by the same kind of agent, and 9/10 held up
  exactly. The discipline that matters is not "distrust all subagent
  output" but "never let a citation skip the dedicated verification step
  before being asserted as fact in framework.md."

**Corrections applied:**
- Fixed Swanson's venue/date and the specific list of his four stated
  objections; removed the double-attribution of the KMS-circularity point.
- Added a v2.1 status-log line in framework.md recording the clean
  verification result (9/10 exact, 1 minor fix, 0 fabrications) for future
  reference.

**Open objections (carried forward):**
1. Condition (c) (modular-Hamiltonian coupling) is still unoperationalized —
   no citation search has been run specifically against this proposed fix
   yet (it's my own candidate wording, not yet checked against literature).
2. No concrete toy model has been built or computed. This remains the
   single biggest gap between "well-cited literature synthesis" and "a
   checkable research result" (novelty referee's point, unresolved).
3. De la Hamette's diagonal Rényi invariants as a possible fix for the
   QRF-relativity problem in condition (b2) have not been attempted.

**Decision point:** two full rounds (4-referee adversarial pass + dedicated
citation check) have now run. Round 1 found and fixed real, substantive
errors (2 wrong citations, 1 false claim of immunity, 1 overclaimed
equivalence class). Round 2 found only one minor, non-fatal correction and
zero new fabrications — i.e., the rate of newly discovered defects dropped
sharply between rounds, which is the actual convergence signal "loop till
success" should be tracking (not "zero defects found," which is too strong
a bar for a document citing ~25 sources, but "diminishing, non-fatal
defects"). One more holistic round is warranted before declaring success:
a fresh adversarial pass against the *whole* v2.1 document (not a specific
objection) asking only "is there any remaining fatal flaw, or does this now
hold up as an honest, correctly-scoped research proposal?" — see round 3.

---

## Round 3 (2026-10-10) — final holistic whole-document pass (convergence check)

A sixth fresh agent read framework.md and self_critique.md end to end (not
one narrow slice) and was asked a single question: is there a remaining
fatal flaw, or does the document now hold up as an honest, scoped research
proposal?

**Connections found:**
- The clearest finding of the whole project: condition (a) ("the reduced
  state is KMS/thermal") and the definition of A (`D_KL` between forward and
  reverse path distributions, i.e. KPV entropy production) are in direct
  tension, because a KMS/stationary state has forward and reverse path
  distributions that coincide *by definition* — `A ≡ 0` there. Meanwhile T
  keeps advancing. So condition (a), exactly as narrowed in round 1 to
  satisfy the QI referee, quietly broke compatibility with A. This is the
  textbook version of the mandate's own warning: "a fix made for one referee
  can silently break a claim made elsewhere" — and it took a *holistic*
  reader, not another narrow specialist, to see it, because rounds 1-2 each
  owned one slice (GR, QI, philosophy, novelty, citations) and none of them
  re-audited the whole condition set after each individual fix.
- The resolution connects directly to Erker et al. (PRX 2017, already cited
  in Bridge C′ since round 1) — their entropy-production-vs-accuracy
  tradeoff for autonomous quantum clocks is precisely the physics of "a
  non-equilibrium recording device coupled to a stationary reference," which
  is exactly the fix condition (a)/(c) needed. The citation was already in
  the document for a different reason; this round is what revealed it was
  also the answer to this structural gap. Worth remembering: a citation
  gathered for one purpose can quietly resolve a problem discovered later —
  re-scan existing citations before searching for new ones.

**Mistakes caught:**
- Condition (a) as written in v2 made Claim 2 internally incoherent in
  exactly the regime it was narrowing toward (A collapses to a constant
  while T advances, so no affine map between them is meaningful). This was
  not a citation error or a missing rebuttal like rounds 1-2 found — it was
  a genuine logical/physical inconsistency introduced *by my own round-1
  edit*, while fixing a different referee's objection. **Lesson distinct
  from round 1's lesson:** round 1 taught "verify citations before trusting
  them." Round 3 teaches "re-audit the whole claim after any local fix,
  because local fixes can break non-local consistency." These are different
  failure modes and both need a standing check, not just the first one.
- Minor: a symbol collision (horizon area vs. the entropy-production leg,
  both called "A") existed since v1 and was never flagged until a reader
  went through the whole document in one pass rather than one critique
  thread at a time.

**Corrections applied:**
- Split condition (a) into "the KMS state defining Θ" vs. a separate,
  non-equilibrium recording subsystem that defines A and R; folded this into
  condition (c), which now constrains both A and R's apparatus instead of R
  alone.
- Disambiguated the symbol collision (`𝒜_horizon` vs. `A`).
- Added an explicit conjectural/unvalidated tag directly on Claim 2's own
  header (previously the hedging was present but two paragraphs downstream,
  not load-bearing at the point of the claim itself).
- Cross-referenced the (b1)-circularity finding from Claim 2's condition
  list directly, rather than leaving it to be found only in the separate
  critique table.

**Open objections (carried forward, now sharper than round 2 left them):**
1. Condition (c) is unoperationalized, and round 3 made it a harder target:
   it must now operationalize a working non-equilibrium recorder *and* its
   modular-Hamiltonian coupling, not just the coupling alone.
2. No toy model exists yet. Round 3 identifies the likely obstacle a toy
   model would hit first (the A/equilibrium tension above) before anyone
   attempts to build one — this is more useful than round 1-2's generic
   "build a toy model" ask, because it names the first wall a toy model
   would run into.
3. De la Hamette's diagonal Rényi invariants as a QRF-fix for (b2): still
   untried.

## Round 4 (2026-10-10) — first computational round, triggered by a new /goal

The user set a new goal after the repo was first published: operationalize
condition (c), build an actual computable toy model, and test the proposed
fix for the QRF/observer-dependence problem (condition b2). This is the
first round where the project computed anything rather than argued from
literature and logic.

**Connections found:**
- Erker et al.'s autonomous-clock paper (cited since round 1 for a different
  reason — the A-vs-accuracy tradeoff) turned out to be the literal physical
  mechanism needed to fix the round-3 structural gap: their clocks use a
  semi-infinite tape of fresh ancillas specifically because a single fixed
  readout system saturates. I didn't need a new citation search to find the
  fix — I needed to re-read a citation already in the document with the new
  problem in mind. Second time this exact pattern has shown up (round 3 made
  the same observation about this same paper, in the abstract/theoretical
  register; round 4 is what happens when you actually build the thing the
  theory predicted and watch it saturate in real numbers).
- This connects to "collision models" (Ciccarello, Lorenzo, Giovannetti &
  Palma, Phys. Rep. 2022, arXiv:2106.11974 — verified by search this round),
  a named, standard architecture in quantum thermodynamics for exactly the
  "periodically-refreshed ancilla" mechanism the toy model needed. Grounding
  an ad hoc numerical trick (reset R every Δτ) in an established modeling
  framework, rather than presenting it as a one-off hack, is the difference
  between a defensible result and an arbitrary one.
- De la Hamette's actual theorem (fetched via WebFetch this round, not
  re-used from round 2's paraphrase) is stated at a pure group-theory level
  with NO worked example in the paper itself — meaning the toy model built
  this round to test it is a genuinely original numerical illustration, not
  a duplication of anything published, regardless of whether the test
  succeeded.

**Mistakes caught / near-misses:**
1. **A hypothesis was wrong, and the first instinct to force a story around
   it was resisted.** Before running `toy_model_detector_recorder.py` I
   expected (and wrote into the code's docstring as a comment) that a static
   recorder, slowly coupled, would show a long plateau of sustained nonzero
   A and R due to timescale separation. The actual numbers showed a peak
   followed by *continuous decay toward zero*, not a plateau — the
   hypothesis was simply wrong. Correct response (taken): report what the
   code actually produced, not what was expected, and use the surprise to
   motivate the next experiment (the tape fix) rather than silently
   adjusting the narrative to make the first guess look right.
2. **The QRF toy model's first construction gave a result and it would have
   been easy to over-report it.** The restricted 2-sector family gave a
   clean "frames agree" result — which, if reported alone, would have
   looked like a success for the de la Hamette fix. Catching that this
   family has an accidental exchange symmetry unrelated to the cited
   theorem (and re-testing on a generic 4-sector family, where it then
   *failed* to match) is exactly the kind of self-adversarial check that a
   narrower, less careful pass would have skipped. **This is the single
   most important process event of round 4**: a positive-looking result was
   not accepted at face value before checking whether the test was actually
   meaningful.
3. When the generic-state QRF test then failed to match even after
   dephasing, there were two bad options available and both were rejected:
   (a) quietly tweak the construction until it matches (data-dredging a
   positive result), or (b) report "the de la Hamette fix doesn't work" as
   if the toy model's own validity were established (a false negative
   presented as a strong claim). Instead: reported as inconclusive, with
   the specific, falsifiable reason given (Rényi entropy is already
   permutation-invariant on a diagonal matrix, so a mismatch in the
   diagonal multiset itself can't be explained by the theorem's "exists a
   permutation" clause — meaning either the construction isn't an "ideal
   frame" in the paper's technical sense, or something else is missing).
   This keeps the door open for a future, better-constructed test instead
   of closing it with an unearned verdict in either direction.
4. Condition (c)'s "commutes with the modular generator" sub-clause was
   written into `framework.md` v2.2 as if it would obviously matter. The
   toy model showed it did *not* visibly matter at the coupling strength
   tested (both commuting and non-commuting couplings preserved the clock's
   KMS-ness equally well). Rather than drop the clause or claim it was
   wrong, it's now explicitly flagged as untested-at-these-parameters,
   because the honest situation is "we don't yet know the threshold," not
   "the clause is false."

**Corrections applied (all in `framework.md` v3, `toy_model.md` new):**
- Condition (c) rewritten to foreground the now-numerically-confirmed
  "renewable apparatus / tape" requirement, with the modular-generator
  commutation clause demoted to an explicitly open, untested refinement.
- Condition (b2) updated to report the QRF test as inconclusive, with the
  specific technical reason the test doesn't resolve the question, rather
  than silently leaving the prior round's "untried" status unchanged or
  overstating a result either way.
- New `toy_model.md`, three new Python scripts, and CSV outputs added to
  the repo so every number above is independently reproducible.

**Open objections (carried forward):**
1. The commutation-with-modular-generator threshold for condition (c) was
   not found — needs a parameter sweep over `g/Γ0`, not yet run.
2. Condition (b2)'s fix remains untested in any confirmed sense. Next step
   (if pursued): either reconstruct de la Hamette's "ideal frame" formalism
   more faithfully (it likely requires the frame to carry a full/faithful
   representation of the symmetry group, which a bare qubit may not), or
   find/build a different minimal example that more clearly satisfies her
   preconditions, before drawing any conclusion about the fix itself.
3. The toy models' own correctness (the physics, not just the citations)
   has only been checked by the one person/process that built them. Given
   this project's standing rule (verify before trusting), the code and its
   physical setup should get the same adversarial-review treatment the
   prose claims got in rounds 1–3 before being treated as settled — this is
   the natural next action, not yet done as of this entry.

**Convergence decision:** round 3 found **no fatal flaw** — i.e., nothing
that invalidates Claim 1 (still fully established and verified) or Claim 2's
honest framing as an unvalidated conjecture with named, specific residual
gaps. It found one important *structural* gap (the A/KMS tension), which has
now been fixed, and several small clarity items, also now fixed. Three
successive rounds show a clear, monotonically decreasing severity trend:
round 1 found 2 wrong citations + 1 false immunity claim + 1 overclaimed
equivalence class (multiple substantive/fatal-adjacent errors); round 2
found 1 minor misattribution and zero fabrications; round 3 found 1
structural-but-fixable gap and zero wrong citations or factual errors. This
is the convergence criterion stated at the end of round 2, now satisfied:
**declaring the adversarial-review loop complete.** The document (v2.2) is
an honest, correctly-scoped, now internally-consistent research proposal.
It is explicitly NOT a validated result, a submittable paper, or a claim
that new physics has been discovered — that status is accurate and should
not be inflated in any future session that picks this project back up. The
three concrete next steps for anyone continuing this work are, in priority
order: (1) operationalize condition (c) with the A/R split now made explicit,
(2) build the toy model (Unruh–DeWitt detector or two-mode Gaussian thermal
state, per the novelty referee's round-1 suggestion), watching for the A/KMS
obstacle identified in round 3, (3) check whether de la Hamette's diagonal
Rényi invariants rescue condition (b2) from QRF-relativity.
