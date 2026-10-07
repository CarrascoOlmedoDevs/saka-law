# Event log

A dated record of external events relevant to the framework. **Logging an event does not change the paper.** Changes of method go to [`pending-changes.md`](../pending-changes.md) and enter the paper only at a scheduled revision (see the release policy there). This follows the specification's rule to update "at fixed intervals rather than after emotionally salient news".

Each entry gives the event, its primary source, the framework element it bears on, and what was done. Dates are those of the event, not of logging.

| Date | Event | Source | Bears on | Action |
|---|---|---|---|---|
| 2024-10-13 | Starship Flight 5: first Super Heavy booster caught by the launch tower (background for recovery milestones) | SpaceX | $S$ (reuse) | Context only |
| 2026-04-14 | Cursor and NVIDIA: multi-agent system optimizes 235 CUDA kernels for Blackwell, 38% geometric-mean speedup vs baseline PyTorch, on a benchmark platform | [StartupHub](https://www.startuphub.ai/ai-news/technology/2026/ai-agents-boost-gpu-kernels-38) | Closed-loop channel (AI → kernels → compute cost); adoption not shown | Logged; pending change 14 applies |
| 2026-05-22 | FastKernels (Snowflake): in production serving, the best AI kernel agent reaches 0.94× of vLLM/SGLang baselines; only 20% of winning kernel sets run correctly as-is | [Pith](https://pith.science/paper/2605.23215) | Benchmark gains vs adoption; validation bottleneck in engineering | Logged; evidence for pending change 14 |
| 2026-06-24 | OpenAI–Broadcom "Jalapeño" inference chip: OpenAI models used to accelerate parts of design and optimization; nine months to tape-out; performance per watt not yet published | [OpenAI](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/) | Closest candidate for closed loop (AI → its own hardware); AI share and gain unmeasured | Watch for technical report |
| 2026-07-24 | Starship Flight 13: ship performs in-space relight and precise controlled splashdown, survives intact for the first time; booster lost on landing burn | [Wikipedia](https://en.wikipedia.org/wiki/Starship_flight_test_13) | $S$ (reuse milestones) | Logged |
| 2026-08-06 | AMD acquires Taalas, which hardwires model weights into silicon; HC1 runs Llama 3.1 8B at ≈17,000 tokens/s, claimed 73× an H200 at one-tenth the power (vendor claim); one model per chip, ≈2-month re-spin | [SiliconANGLE](https://siliconangle.com/2026/08/06/amd-acquires-taalas-hardwire-ai-models-silicon/) | $C$, $E$, efficiency index $\Pi$; hardware improving AI, not AI improving hardware | Logged |
| 2026-08-10 | Claude raises the proven lower bound on Riemann zeta zeros on the critical line from 41.6% to 67.2%, with Lean formalization | [Anthropic](https://www.anthropic.com/research/riemann-zeta) | P6 baseline (domain a) | Calibration case 2 |
| 2026-09-04 | Complete Lean formalization of Fermat's Last Theorem, largely by Claude | [Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | $A$ (formal theorem proving); not a discovery | Calibration case 4 |
| 2026-09-08 | OpenAI: finite-time blowup for forced 3D Navier–Stokes, with Lean formalization | OpenAI announcement; Clay statement of 11 Sep | P6 baseline (domain a) | Calibration case 3 |
| 2026-09-22 | Epoch AI: cost of a fixed AI capability level falls ≈47% per quarter since 2023 | [Epoch AI](https://epoch.ai/publications/the-plunging-price-of-thought) | $A$, HTAB, maturity-aligned TAR | Merged in v0.3.3 |
| 2026-09-28 | Starship Flight 14: first orbital mission; 26 Starlink V3 deployed; ship splashdown after ≈2 orbits; booster splashdown then deliberately destroyed; no ship catch attempted | [NASASpaceFlight](https://www.nasaspaceflight.com/2026/09/starship-14-orbit-flight-15/) | $S$; change point requires reflight of recovered vehicles | Logged |
| 2026-10-01 | Sinclair laboratory: "v2" reprogramming pilot in LAKI (progeroid) mice, >33% maximum lifespan, unpublished | X (@davidasinclair) | LTI L2; no update to $G_j$ | Recorded in `forecasts/er100-2026-10-08.md`, section 4 |
| 2026-10-01 | Life Biosciences announces first-in-human ER-100 data for 8 Oct | [BioSpace](https://www.biospace.com/press-releases/life-biosciences-to-present-first-in-human-data-from-ongoing-phase-1-trial-evaluating-er-100-in-optic-neuropathies-at-eyecelerator-2026) | LTI L4; $G_j$ for partial reprogramming | Pre-commitment `forecasts/er100-2026-10-08.md` |
| 2026-10-01 | Google Project Suncatcher: four TPUs launched on a Planet Labs satellite (Falcon 9) to test radiation, heat rejection, power and inter-satellite links for orbital AI compute | [Seoul Economic Daily](https://en.sedaily.com/international/2026/10/02/google-launches-satellite-carrying-four-tpus-to-test-ai) | Coupling of $S$ with $E$ and $C$ | Pending change 15 |
| 2026-10-05 | Alman & Vassilevska Williams: truly subquadratic 3SUM and subcubic APSP; core algorithm found by a Claude research model without human input | [arXiv:2610.06783](https://arxiv.org/abs/2610.06783) | P6 baseline (domain a, importance 3 provisional) | Calibration case 5 |
| 2026-10-06 | OpenAI releases 722 manuscripts (372 result families) produced by an internal model; 162 papers with formalized main results; formal statements not yet human-reviewed | [github.com/openai/math](https://github.com/openai/math) | P6 baseline; verification as bottleneck ($Q_t$) | Batch entry below; pending changes 11–13 |
| 2026-10-07 | ≈4,000 | 372 | 722 | 162 (185 main-result declarations) | 0 (catalogue review status: "unchecked") | 0 known | 0 known |

### Reading under the framework

- **P6 today:** zero replicated discoveries from this batch. All 372 families are *candidates* logged in the pre-freeze baseline.
- **Generation vs validation:** results were produced in weeks at hours of compute each; verification proceeds at the pace of human review. The counters above are a direct measurement of validated throughput $Q_t$ in mathematics and of the verification bottleneck described in Section 9 of the paper.
- **Hit rate:** 372 families from about 4,000 problems posed (≈9% before verification). The verified hit rate will be the number to compare with future batches.
- **Conflict of interest:** the developer reports its own results. The person maintaining this log works with a Claude model (Anthropic), a competitor of the developer; both directions of bias are possible.
