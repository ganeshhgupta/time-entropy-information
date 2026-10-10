# Is time an emergent property of information?

A research framework asking a narrower, answerable question: when physics
talks about "time," it's conflating at least three different things —
**relativistic proper time** (geometric, part of the metric), **thermodynamic
time** (the statistical entropy-increase arrow), and **informational time**
(orderings built from quantum correlations and records). This project states
precisely how they relate, which parts are established physics and which
are conjecture, and tests the conjecture computationally.

Built through five rounds of adversarial review (independent referees
attacking the claims, a dedicated citation-verification pass, a holistic
whole-document read, and — once code entered the picture — an adversarial
code/physics audit that caught a real bug). Nothing here is asserted without
either a citation someone independently checked, or a number someone's code
actually produced.

## Start here

| File | What it is |
|---|---|
| [`CONTINUE.md`](CONTINUE.md) | **Read this first.** Orientation for picking this up with zero prior context — what's settled, what's open, what to do next. |
| [`framework.md`](framework.md) | The actual research content: the three-notions-of-time distinction (established), and a four-quantity coincidence conjecture (partially novel, partially already published, now partially computationally confirmed). |
| [`toy_model.md`](toy_model.md) | What was actually computed: an Unruh–DeWitt-type detector + recorder qubit toy model, run and audited. |
| [`self_critique.md`](self_critique.md) | The full reasoning log — every mistake caught, every connection found, across 5 rounds. Read this before second-guessing anything in `framework.md`. |
| [`BIBLIOGRAPHY.md`](BIBLIOGRAPHY.md) | Every source, in the order it entered the reasoning, tagged VERIFIED / REPORTED / RETRACTED. |

## Running the toy models

```
python3 toy_model_detector_recorder.py   # base case: static recorder
python3 toy_model_tape_recorder.py       # fix: periodically-refreshed recorder
python3 toy_model_qrf_invariant.py       # test of a proposed QRF-relativity fix
```

Pure NumPy/SciPy, no QuTiP required. Each script regenerates its own CSV
output from scratch in under a minute.

## Headline result so far

A recording apparatus sustains a genuine, steady informational "clock tick"
(nonzero entropy production *and* nonzero recoverable mutual information)
indefinitely, while a thermal/modular time parameter stays well-defined,
only when it satisfies three joint conditions — renewable, commuting with
the reference system's own Hamiltonian, and informationally (not just
thermodynamically) active. All three were confirmed together in one
computable toy model. A separate proposed fix for reference-frame-dependence
was tested and found genuinely inconclusive, reported as such rather than
forced to an answer.

## Status

This is an adversarially-reviewed **research proposal**, not a validated
physical result, new physics, or a submittable paper. See `CONTINUE.md` for
exactly what would need to happen next, and `self_critique.md` for why that
framing is deliberate, not modesty.
