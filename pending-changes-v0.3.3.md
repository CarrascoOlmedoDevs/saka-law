# Pending changes for v0.3.3

`paper.md` and `model-spec.md` on `main` match the version archived on Zenodo as v0.3.2 ([DOI 10.5281/zenodo.23092958](https://doi.org/10.5281/zenodo.23092958)). Changes agreed since then are collected here and will be merged into the paper and specification at the next release.

Each entry records the case that motivated it.

---

## 1. LTI indexed by intervention × indication

**Motivation (2 Oct 2026):** GLP-1 receptor agonists. Semaglutide has demonstrated clinical benefit (L8) for obesity and cardiovascular risk, but for "slowing ageing" the evidence is at L2–L3: a lifespan effect in mice confounded by weight loss, and epigenetic-clock effects in one special population that were not seen in healthy older adults.

**Change:** assign LTI levels, EMS and the readiness factor $G_j$ to the pair *(intervention, indication)*, not to the intervention alone.

**Consequence for P7 and P8:** repurposing an already-approved drug for an ageing indication does not count as faster translation unless it is measured within its own (intervention, indication) stratum; otherwise approvals of repurposed drugs would make translation look faster by construction.

## 2–5. AI attribution scale

**Motivation (3 Oct 2026):** calibration case 1 in [`ai-attribution/calibration-cases.md`](./ai-attribution/calibration-cases.md) (Sinclair laboratory public statements).

2. **Unit of analysis.** Code discoveries documented in a publication or preprint. Statements in interviews, blogs or social media are recorded as claims and not coded.
3. **Search-space rule.** If AI generates or ranks candidates within a target space chosen by humans, the maximum level is $AI_2$. $AI_3$ requires that AI proposed the hypothesis or target itself.
4. **Speed claims are not evidence.** Acceleration enters only as measured SCT or $Q_t$ from dated records.
5. **Source quality.** Record whether sources are primary or secondary; only primary sources can support a level above $AI_1$.

## 6. HTAB aligned by maturity, not only by calendar

**Motivation (3 Oct 2026):** Epoch AI, ["The plunging price of thought"](https://epoch.ai/publications/the-plunging-price-of-thought) (22 Sep 2026). The cost of reaching a fixed level of performance on reasoning benchmarks fell about 47% per quarter (≈13× per year) from 2023, which the authors report as 6× faster than compute and 4× faster than DNA sequencing.

**Problem:** that comparison sets three years of a new technology against decades of mature ones. Most technologies fall fastest in cost early in their life (Wright's law); DNA sequencing also fell much faster than Moore's law in its first years of next-generation sequencing. A high TAR for a young series can therefore reflect its stage, not a change of regime.

**Change:**

- For each HTAB series, record its introduction date and, where available, cumulative production.
- Report $TAR_i$ in two forms: **calendar-aligned** (current window against the series' own history, as now) and **maturity-aligned** (a young series against other technologies over the *same number of years since introduction*, or the same multiples of cumulative production).
- A claim of acceleration for a young technology requires the maturity-aligned $TAR$ to exceed 1, not only the calendar-aligned one.

## 7. New data source and test for the $A$ component

**Source:** Epoch AI, "The plunging price of thought" (as above), and its underlying data.

**Use:**

- Candidate series for the HTAB and for a cost-efficiency sub-measure of $A$ (cost of a fixed capability level), alongside the capability sub-measures.
- Caveats to record with it: three years of data; benchmarks may be targeted in training; prices include market margins and are not pure costs; results range from 43% to 58% per quarter depending on the averaging method.

**Proposed test (candidate supplement to P2/P4).** Epoch reports that, for each performance level, cost falls fastest when the level first appears (≈66% per quarter) and slows afterwards (≈32% per quarter after two years). That within-level slowdown is a normal learning curve and says nothing about acceleration. The test relevant to the Saka Law is **across cohorts**: whether the *debut* rate of cost decline rises for successive performance levels as they appear over time. A rising debut rate would be evidence of acceleration in AI efficiency; a constant one would indicate a fast but ordinary exponential.

This test concerns the efficiency of an AI input. On its own it does not bear on validated discovery (Section 9 of the paper).

## 8. Candidate HTAB series: power electronics

**Motivation (2 Oct 2026):** discussion of gallium nitride (GaN) power devices.

**Change:** consider adding cost per watt and conversion efficiency of power semiconductors (GaN, SiC) as an HTAB series relevant to $E$. Record gallium supply concentration and export controls as a BPI item (geopolitical disruption), not as part of $E$.

## 9. AI attribution: three further refinements

**Motivation (6 Oct 2026):** calibration cases 2–4 (Riemann zeta bound, Navier–Stokes, Fermat formalization).

- Formalizing a known result is a capability event for $A$, not a discovery.
- A machine-checked proof counts as replication only after humans confirm that the formal statement matches the claimed theorem.
- Conflicts of interest between an AI coder and the system being coded are flagged; the human coding is done first in those cases.

## 10. P6: count only from a frozen baseline, and weight by importance

**Motivation (6 Oct 2026):** at least three candidate $AI_3$/$AI_4$ results in mathematics in two months (Riemann zeta bound, 10 Aug; Navier–Stokes, 8 Sep; an algorithmic-complexity result, 6 Oct, paper not yet identified).

**Problems:**

1. Until the preregistration is frozen, every such event enlarges the **baseline** against which P6 must "at least double". The later the freeze, the higher the bar. The baseline must therefore be counted up to a fixed date and frozen with the thresholds.
2. A raw count treats a tiny improvement on a technical bound the same as the resolution of a central problem.

**Change:**

- P6 reports the count of qualifying discoveries **separately by domain** (mathematics and formal sciences; computational sciences; experimental sciences), because mathematics is the domain where AI can work without physical validation and would dominate a pooled count.
- Each discovery also receives a preregistered **importance grade** (e.g. 1 = incremental improvement of a known bound; 2 = resolution of a recognized open problem; 3 = resolution of a central problem of the field), assigned by the same two-coder procedure. P6 is reported both as a raw count and as an importance-weighted count; the hypothesis is supported only if the experimental-sciences count also rises.
- The baseline period for P6 ends on the preregistration date; candidate events before that date are logged in `ai-attribution/` as baseline events.

---

## Open items not yet decided

- **ER-100 outcome file.** After 8 October 2026, record the result in `forecasts/er100-2026-10-08-outcome.md` and score predictions E1–E8 (see [`forecasts/er100-2026-10-08.md`](./forecasts/er100-2026-10-08.md)).
- **Human second coder** for the AI attribution calibration cases.
