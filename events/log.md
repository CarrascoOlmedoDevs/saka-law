# Event log

A dated record of external events relevant to the framework. **Logging an event does not change the paper.** Changes of method go to [`pending-changes.md`](../pending-changes.md) and enter the paper only at a scheduled revision (see the release policy there). This follows the specification's rule to update "at fixed intervals rather than after emotionally salient news".

Each entry gives the event, its primary source, the framework element it bears on, and what was done. Dates are those of the event, not of logging.

| Date | Event | Source | Bears on | Action |
|---|---|---|---|---|
| 2026-08-10 | Claude raises the proven lower bound on Riemann zeta zeros on the critical line from 41.6% to 67.2%, with Lean formalization | [Anthropic](https://www.anthropic.com/research/riemann-zeta) | P6 baseline (domain a) | Calibration case 2 |
| 2026-09-04 | Complete Lean formalization of Fermat's Last Theorem, largely by Claude | [Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | $A$ (formal theorem proving); not a discovery | Calibration case 4 |
| 2026-09-08 | OpenAI: finite-time blowup for forced 3D Navier–Stokes, with Lean formalization | OpenAI announcement; Clay statement of 11 Sep | P6 baseline (domain a) | Calibration case 3 |
| 2026-09-22 | Epoch AI: cost of a fixed AI capability level falls ≈47% per quarter since 2023 | [Epoch AI](https://epoch.ai/publications/the-plunging-price-of-thought) | $A$, HTAB, maturity-aligned TAR | Merged in v0.3.3 |
| 2026-10-01 | Sinclair laboratory: "v2" reprogramming pilot in LAKI (progeroid) mice, >33% maximum lifespan, unpublished | X (@davidasinclair) | LTI L2; no update to $G_j$ | Recorded in `forecasts/er100-2026-10-08.md`, section 4 |
| 2026-10-01 | Life Biosciences announces first-in-human ER-100 data for 8 Oct | [BioSpace](https://www.biospace.com/press-releases/life-biosciences-to-present-first-in-human-data-from-ongoing-phase-1-trial-evaluating-er-100-in-optic-neuropathies-at-eyecelerator-2026) | LTI L4; $G_j$ for partial reprogramming | Pre-commitment `forecasts/er100-2026-10-08.md` |
| 2026-10-05 | Alman & Vassilevska Williams: truly subquadratic 3SUM and subcubic APSP; core algorithm found by a Claude research model without human input | [arXiv:2610.06783](https://arxiv.org/abs/2610.06783) | P6 baseline (domain a, importance 3 provisional) | Calibration case 5 |
| 2026-10-06 | OpenAI releases 722 manuscripts (372 result families) produced by an internal model; 162 papers with formalized main results; formal statements not yet human-reviewed | [github.com/openai/math](https://github.com/openai/math) | P6 baseline; verification as bottleneck ($Q_t$) | Batch entry below; pending changes 11–13 |

---

## Batch entry: OpenAI mathematics collection (6 October 2026)

**Source:** [github.com/openai/math](https://github.com/openai/math), initial commit 6 October 2026 (~22:00 UTC); README, `CONTENTS.md`, `lean/formalization.yaml`.

**What it is.** Manuscripts produced by an unreleased internal OpenAI model during evaluation on open research problems. About 4,000 problems were posed; on average each result used about three hours of model compute; outputs were grouped into families and filtered by significance. Two results (a zero-free region for the Riemann zeta function, and the Hodge conjecture for CM abelian varieties) were produced outside this fixed procedure, and one write-up was edited by humans for readability. The README states that some unformalized results "could have issues".

**Claimed results include** (unverified; listed only to show scale): the full Birch–Swinnerton-Dyer formula for elliptic curves over ℚ with Selmer corank 0 or 1 for some prime; symmetric and general Mahler conjectures; isomorphism of free group factors; Kaplansky's direct-finiteness conjecture in characteristic two; a zero-free region Re(s) > 11/12 for the Riemann zeta function.

**Why it is logged as one batch, not coded case by case.** Coding hundreds of claims before the mathematical community has examined them would add noise, not information. What the framework needs is how many of these claims survive verification, and how fast.

### Counters

To be updated at each scheduled revision. "Human-verified" means that an independent expert or a peer-reviewed publication has confirmed the result, or that humans have confirmed that a formal statement matches the claimed theorem (attribution rule 6).

| As of | Problems posed | Result families | Manuscripts | Papers with formalized main result | Formal statements human-reviewed | Families human-verified | Families withdrawn or found wrong |
|---|---|---|---|---|---|---|---|
| 2026-10-07 | ≈4,000 | 372 | 722 | 162 (185 main-result declarations) | 0 (catalogue review status: "unchecked") | 0 known | 0 known |

### Reading under the framework

- **P6 today:** zero replicated discoveries from this batch. All 372 families are *candidates* logged in the pre-freeze baseline.
- **Generation vs validation:** results were produced in weeks at hours of compute each; verification proceeds at the pace of human review. The counters above are a direct measurement of validated throughput $Q_t$ in mathematics and of the verification bottleneck described in Section 9 of the paper.
- **Hit rate:** 372 families from about 4,000 problems posed (≈9% before verification). The verified hit rate will be the number to compare with future batches.
- **Conflict of interest:** the developer reports its own results. The person maintaining this log works with a Claude model (Anthropic), a competitor of the developer; both directions of bias are possible.
