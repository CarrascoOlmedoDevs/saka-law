# AI attribution scale — calibration cases

This file collects worked examples for the $AI_0$–$AI_4$ attribution scale (paper Section 9; model specification Section 6.1). Its purpose is to test the definitions on real, difficult cases **before** the pilot coding begins, and to record the refinements those cases suggest.

Calibration cases are not part of the P6 count. They are chosen because they are informative, not because they are representative.

**Coding rules recalled** (from the specification): levels are assigned from author-contribution statements and methods sections by two independent coders blind to the prediction; disagreements resolve to the lower level; only $AI_3$ and $AI_4$ count toward P6.

**First coder for the cases below:** an AI system (Claude). Under the protocol, the second coder must be human. Every coding below is therefore **provisional until a human coder has coded the case independently**, without seeing this coding first.

---

## Case 1 — Sinclair laboratory (Harvard), public statements on AI use, 2025–2026

**Added:** 3 October 2026.

### Sources

| Date | Source | Type |
|---|---|---|
| 3 July 2025 | [Diamandis blog, "AI is Accelerating Longevity Research Millions-Fold"](https://www.diamandis.com/blog/ai-is-accelerating-longevity-research-millions-fold) | Interview write-up on a promotional blog |
| 7 August 2026 | [BigGo Finance, "The First Human Age-Reversal Trial Is Underway, and AI Just Made It Faster"](https://finance.biggo.com/news/f6e9b6ea1ee30825) | News aggregator summarizing an interview |
| 30 Sep – 1 Oct 2026 | David Sinclair on X (@davidasinclair): announcement of "v2" reprogramming technology and LAKI-mouse pilot | Social media |

None of these is a primary scientific source. No publication, preprint or methods section describing the AI work was found.

### Statements and provisional coding

| # | Reported use of AI | Provisional level | Reasoning |
|---|---|---|---|
| 1a | Virtual screening of "trillions" of theoretical molecules by docking against enzyme structures predicted with AI protein-structure tools; about 100 top candidates selected for testing | $AI_1$–$AI_2$ | AI executes and ranks a screen whose targets and strategy were chosen by humans. Prioritizing candidates is partial design ($AI_2$) at most. The hypothesis being tested (restoring epigenetic information reverses ageing) predates the screen. |
| 1b | Image-based algorithm estimating cellular age from microscope images | $AI_1$ | Measurement and data analysis on a human-designed study. |
| 1c | A summer intern using AI found "the smoking gun" for the location of a cellular "backup copy" of youth | **Not codable** | No description of the task, the AI system's role or the result. |
| 1d | A "cocktail of three molecules" acting on four ageing pathways, identified with AI | **Not codable yet** | Composition undisclosed; unclear whether AI chose the combination or only screened single molecules. If this is the "v2" drink announced on 1 October 2026, it is unpublished (LTI level L2, progeroid mice). |
| 1e | ER-100 (OSK gene therapy, Phase 1 trial NCT07290244) | $AI_0$ or none | OSK derives from the Yamanaka factors (2006) and earlier partial-reprogramming work (Ocampo et al. 2016). No AI role in the core hypothesis has been reported. |

**Speed claims, recorded separately and not coded.** "What we do now in a month would've taken thousands of years"; a screen that "would have taken 160 years" done in two months; "we're now eight years ahead of what the public realizes". These describe computational screening throughput. They are not measurements of Scientific Cycle Time or validated throughput $Q_t$, which require the time from candidate to validated result.

### Result

**No item reaches $AI_3$ or $AI_4$. Nothing in this case would count toward P6.**

### What would change the coding

- A publication or preprint whose methods and CRediT statements specify which decisions AI made (target choice, hypothesis, combination design, experiment design).
- Evidence that the AI system, not the researchers, selected the target or proposed the combination — that would move 1a/1d towards $AI_3$.
- Hit rates of AI-screened candidates in cell and animal validation, compared with a conventional screen.
- Dated milestones from candidate selection to validated in vivo result, which would give a real SCT data point.
- Independent replication of the resulting compound's effect, required for P6.

---

## Case 2 — Riemann zeta function: proportion of zeros on the critical line (Anthropic, August 2026)

**Added:** 6 October 2026. **Conflict of interest:** the first coder is a Claude model and this result was produced by a Claude model. The human second coding is especially important for this case.

**Source (primary):** Anthropic, ["Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis"](https://www.anthropic.com/research/riemann-zeta), 10 August 2026, with a paper and a Lean formalization.

**What was done:** an unreleased research version of Claude raised the proven lower bound on the proportion of non-trivial zeros on the critical line from 41.6% to 67.2%.

**Roles reported:** a non-mathematician staff member asked the model to attempt the problem and encouraged it to continue; the model ran two Claude Code sessions (about 31 million output tokens, roughly 60 sub-agents in the second); two Anthropic mathematicians checked the result and two external experts examined the paper. The model also produced a Lean formalization.

**Provisional level:** $AI_4$ for the intellectual work (problem attacked, method chosen, proof constructed and formalized by the model; humans limited to prompting and verification). It may be $AI_3$ if the paper shows that humans chose the method.

**Counts toward P6?** It would, as a pre-freeze **baseline** event, once (a) independent human verification is published or the paper is accepted, and (b) the Lean statement is confirmed to match the claimed theorem. Machine-checked proof satisfies the replication requirement for mathematics only if the formal statement is checked by humans.

**Importance:** a large improvement on a bound that had moved slowly for decades, but, as Anthropic notes, it does not lead to a proof of the Riemann hypothesis.

---

## Case 3 — Navier–Stokes finite-time blowup with forcing (OpenAI, September 2026)

**Added:** 6 October 2026.

**Sources (primary and secondary):** OpenAI, "On the Navier–Stokes Millennium Prize Problem", 8 September 2026, with manuscript and Lean formalization; Clay Mathematics Institute statement of 11 September 2026 (problem "apparently settled", evaluation unhurried); press coverage of the priority dispute.

**What was done:** a proof that a smooth solution of the 3D incompressible Navier–Stokes equations, started from rest and driven by a smooth external force, can blow up in finite time. The unforced case remains open.

**Roles reported:** an internal OpenAI model running about 10,000 agents for 88 hours produced the proof; another model produced the Lean formalization; the method builds on a 2023 construction by Córdoba and Martínez-Zoroa. OpenAI started the effort after hearing that human researchers might be close to related results.

**Provisional level:** $AI_3$–$AI_4$. The proof was constructed by the system, but humans chose the problem and the approach builds directly on prior human work. The coding depends on how much of the construction was directed by humans, which the public material does not fully settle.

**Counts toward P6?** As a pre-freeze baseline event, once independent verification is published. Its importance is high (a Millennium Prize formulation), but the forced case is the more tractable one.

---

## Case 4 — Fermat's Last Theorem formalization (Anthropic, September 2026)

**Added:** 6 October 2026. Same conflict of interest as case 2.

**Source (primary):** Anthropic, ["Formalizing Fermat's Last Theorem"](https://www.anthropic.com/research/formalizing-fermats-last-theorem), 4 September 2026.

**What was done:** a complete Lean formalization of the existing proof of Fermat's Last Theorem (about 13 million lines, 29,500 intermediate theorems, 11 days), largely autonomous, reviewed by Kevin Buzzard.

**Provisional coding:** **not a discovery** — no new mathematics. It is coded as a capability event for the formal-theorem-proving sub-measure of $A$, not on the attribution scale, and does not count toward P6.

**Why it is a useful calibration case:** it shows that a very large, largely autonomous AI achievement can still be outside P6. Autonomy and novelty are separate questions.

---

## Case 5 — Algorithmic complexity result (6 October 2026) — pending identification

**Added:** 6 October 2026.

**Source (secondary):** Carlos Santana (@DotCSV) on X, 6 October 2026: a paper reports that Claude crossed a theoretical barrier in algorithmic complexity that many works had assumed but not proven; the improvement is described as very small in magnitude but theoretically important, according to people in the field.

**Status:** the paper has not yet been identified, so the case is **not coded**. Under refinement 1 below, a social-media report is a claim until the publication is found.

---

## Refinements suggested by these cases (proposed for v0.3.3)

1. **Unit of analysis.** The scale codes *discoveries documented in a publication or preprint*, not laboratories or claims. Statements in interviews, blogs or social media about how a group uses AI are recorded as **claims** and are not coded, however specific they sound.
2. **Who chose the search space.** If AI generates or ranks candidates within a target space chosen by humans, the maximum level is $AI_2$. $AI_3$ requires that AI proposed the hypothesis or target itself, not only the best item within a human-defined search.
3. **Speed claims are not evidence.** Claims of acceleration enter the framework only as measured SCT or $Q_t$ from dated records, never from statements of how long something "would have taken".
4. **Source quality is recorded.** Each case lists whether its sources are primary (paper, preprint, registry) or secondary (press, interview, social media). Only primary sources can support a level above $AI_1$.
5. **Formalization is not discovery.** Formalizing a known result is a capability event for $A$, not a discovery on the attribution scale (case 4).
6. **Formal proofs replicate only with a checked statement.** A machine-checked proof counts as replication for P6 only after humans confirm that the formal statement matches the claimed theorem (cases 2 and 3).
7. **Conflicts of interest are recorded.** When the AI system that is coding belongs to the same developer as the system being coded, the case is flagged and requires the human coding to be done first.
