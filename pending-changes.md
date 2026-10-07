# Pending changes

Changes of method agreed since the last version. They enter `paper.md` and `model-spec.md` only at the next scheduled revision. External events are recorded in [`events/log.md`](./events/log.md), not here.

Items 1–10 were merged into **v0.3.3** on 6 October 2026; see "Changes from version 0.3.2" at the end of `paper.md`. Numbering continues from there.

## Release policy

**Motivation (7 Oct 2026):** between 2 and 6 October the framework was revised in response to several news items in a row. That contradicts the specification's own rule (Section 11, item 7: update "at fixed intervals rather than after emotionally salient news") and weakens the credibility of the preregistration.

**Rule from now on:**

- Events are logged in `events/log.md` as they happen. Logging does not change the paper.
- Changes of method are recorded here, with the case that motivated them.
- The paper and specification change only at **scheduled revisions**. The next is the revision that accompanies the **preregistration freeze**, planned no later than **31 December 2026**. After the freeze, revisions are quarterly.
- Corrections of factual errors in the paper may be released at any time and are labelled as corrections.

## 11. P6 counts verified result families, not manuscripts

**Motivation (6 Oct 2026):** OpenAI mathematics collection (722 manuscripts in 372 families; see `events/log.md`).

**Change:** the unit of count for P6 is the **result family**: a principal result together with its companion arguments, corollaries and alternative proofs. A family counts only when its principal result is human-verified (rule 6). Families are defined by the coders, not taken from the producer's grouping.

## 12. Record the denominator: problems attempted

**Motivation:** same. The collection reports about 4,000 problems posed for 372 families.

**Change:** for any batch of AI-produced results, record the number of problems attempted where it is reported, and report the **verified hit rate** (verified families / problems attempted) alongside the count. Where the denominator is not reported, record that fact; counts without denominators are flagged as selection-prone.

## 13. Verification latency as a measured quantity

**Motivation:** same. Generation now takes hours per result; verification by experts takes months.

**Change:** for each candidate discovery in domain (a), record the claim date and the verification date, and report the distribution of **verification latency**. This is the mathematical analogue of Scientific Cycle Time and a direct measure of the validation bottleneck. A falling generation time with a constant or rising verification latency is evidence that the bottleneck has moved to validation, as predicted in Section 9.

## 14. Evidence of a closed loop requires adoption and a measured gain

**Motivation (7 Oct 2026):** calibration case 5 (3SUM/APSP, arXiv:2610.06783). The result improves the asymptotic cost of a matrix-product operation, which identifies a *possible* feedback channel (AI → mathematics → algorithms → cheaper compute → better AI). But the improvement is tiny in the exponent ($n^{1.9992}$ vs $n^2$; $n^{2.9995}$ vs $n^3$), and asymptotically faster matrix algorithms have historically not been used in practice because of their large constants. AI compute has become cheaper mainly through hardware, lower numerical precision, optimized kernels and compilers.

**Problem:** the framework does not yet distinguish a discovery that *could* feed back into the production of technology from one that *has* done so. Without that distinction, any AI result touching computation could be read as evidence of recursion.

**Change:** separate two kinds of evidence.

- **Capability evidence:** an AI-originated discovery, coded on the $AI_0$–$AI_4$ scale and counted in P6.
- **Closed-loop evidence:** the discovery has been (1) **adopted** in systems used to build technology — libraries, kernels, compilers, hardware design, laboratory protocols — and (2) that adoption produces a **measured gain** in the cost or speed of producing technology, for example in the cost of a fixed AI capability level, training or inference cost, or SCT in a tracked domain. The gain must be attributable to the adopted discovery, for example through a before-and-after comparison or the adopter's own benchmarks.

Each AI-originated discovery records a **feedback channel** (which part of the technology-production process it could affect) and an **adoption status** (none / prototype / adopted in production, with date and source). Closed-loop evidence is reported separately from P6; the Saka Law's core claim — technology improving the process that produces technology — is supported most directly by closed-loop cases, not by the count of discoveries alone.

**Application to case 5:** capability evidence (P6 candidate); feedback channel: algorithms for matrix products; adoption status: none; closed-loop evidence: no.

## 15. Revisit the weight of space access ($S$) and its coupling with energy and compute

**Motivation (7 Oct 2026):** Google's Project Suncatcher launched four TPUs to orbit (1 Oct 2026) to test solar-powered AI compute in space; Starship reached orbit (Flight 14, 28 Sep 2026) after demonstrating booster tower catches (since 2024) and an intact ship splashdown (Flight 13).

**Problem:** v0.3.3 gives $S$ a weight of 0.05 and justifies it only as an expansion of *experimental* state space (microgravity, crystallization, organoids), with no link to the other components. If orbital compute powered by near-continuous sunlight becomes viable, space access becomes a possible route around the energy bottleneck ($E$) for compute ($C$). Under the CES aggregate, that coupling cannot be represented by a small fixed weight on an independent component.

**Change (to be decided at the scheduled revision):**

- Add **orbital compute capacity** (power or compute deployed in orbit) as a candidate proxy, recorded under $C$ and $E$ rather than only $S$.
- Keep the experimental role of $S$ at its current weight, and test in the sensitivity analysis a variant where launch cost per kg enters the cost of $E$ for compute.
- Define the **change-point signal** for $S$: reflight of a recovered orbital upper stage, and sustained launch cadence, not first orbit or splashdown alone. Track launch cost per kg against the threshold at which orbital compute is claimed to become competitive (to be sourced from Google's Suncatcher analysis, not assumed).

## 16. Separate regulatory from technological acceleration in P7 and P8

**Motivation (7 Oct 2026):** FDA policy changes in 2026 — a stated default of one adequate and well-controlled trial plus confirmatory evidence (NEJM opinion, 18 Feb 2026, not yet formal guidance); the draft "plausible mechanism" framework for individualized therapies (23 Feb 2026); the National Priority Voucher pilot (target reviews of 1–2 months; seven approvals by May 2026); the phase-out of animal-testing requirements (from 2025). Critics warn of shifted safety evidence to the post-marketing phase and of institutional strain.

**Problem:** P7 (faster translation) could be satisfied by lowering evidence requirements rather than by technology improving translation, and P8 (better clinical success) could be inflated by approvals on less evidence. Either would be a **false positive** for the Saka Law, whose claim is about technology improving the process that produces technology.

**Change:**

- Record the **regulatory route** of every approval and programme in the P7/P8 data (standard, accelerated, priority voucher, single-trial basis, plausible-mechanism, breakthrough/fast track) and stratify by it.
- Use **AI-involved programmes as the treatment group** and conventional programmes in the same therapeutic area, modality, regulatory route and period as the comparison group (baseline list in `data/ai-drug-pipeline.csv`). Technological acceleration is the *difference* between the groups under the same rules; a fall in both reflects regulation.
- Track **post-approval outcomes**: withdrawals, new boxed warnings and failed confirmatory trials, by regulatory route. A rise in these offsets any gain in P8.
- Classify regulatory changes that are themselves **enabled by technology** (e.g. replacing animal tests with organoids or in-silico models; accepting digital-twin controls) separately: these count as technological acceleration, because the technology is what made the rule change possible.

---

## Open items

- **ER-100 outcome file.** After 8 October 2026, record the result in `forecasts/er100-2026-10-08-outcome.md` and score predictions E1–E8 (see [`forecasts/er100-2026-10-08.md`](./forecasts/er100-2026-10-08.md)).
- **Human second coder** for the AI attribution calibration cases in [`ai-attribution/`](./ai-attribution/calibration-cases.md), starting with cases 2, 4 and 5, which carry a conflict of interest.
- **Update the counters** of the OpenAI batch entry in `events/log.md` at each scheduled revision.
- **Preregistration.** Candidate $AI_3$/$AI_4$ events before the freeze enlarge the P6 baseline; the freeze should not be delayed without reason.
