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

---

## Open items

- **ER-100 outcome file.** After 8 October 2026, record the result in `forecasts/er100-2026-10-08-outcome.md` and score predictions E1–E8 (see [`forecasts/er100-2026-10-08.md`](./forecasts/er100-2026-10-08.md)).
- **Human second coder** for the AI attribution calibration cases in [`ai-attribution/`](./ai-attribution/calibration-cases.md), starting with cases 2, 4 and 5, which carry a conflict of interest.
- **Update the counters** of the OpenAI batch entry in `events/log.md` at each scheduled revision.
- **Preregistration.** Candidate $AI_3$/$AI_4$ events before the freeze enlarge the P6 baseline; the freeze should not be delayed without reason.
