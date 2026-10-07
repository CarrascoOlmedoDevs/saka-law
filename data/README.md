# Data

Tracking datasets maintained by the project. Each file records the date of its snapshot (`as_of`) and a source for every row. Rows are updated at scheduled revisions; earlier snapshots remain in the git history.

## `ai-drug-pipeline.csv`

Baseline snapshot (7 October 2026) of drug candidates described as AI-discovered or AI-designed, including discontinued programmes.

**Purpose.** Comparison group for predictions P7 and P8 (pending change 16): transition probabilities and times of AI-involved programmes are compared with conventional programmes in the same therapeutic area, modality and regulatory period, so that regulatory acceleration is not mistaken for technological acceleration.

**Columns.** `ai_role_claimed` is what the developer or secondary source claims. `ai_level_provisional` is a coding on the $AI_0$–$AI_4$ scale; it is "unknown" unless a primary source documents which decisions the AI made (attribution rules 1–4). Most entries are expected to be $AI_1$–$AI_2$ (AI-assisted design within a human-chosen target space).

**Aggregate context at snapshot date** (secondary sources, to be checked against primary data):

- About 117 AI-enabled assets in clinical trials across 63 companies (data to December 2025); no FDA approval of an AI-discovered drug as of July 2026.
- Reported success rates (2024 analysis): Phase I ≈80–90% for AI-discovered molecules vs ≈40–65% historically; Phase II ≈40%, similar to conventional programmes.

**Limitations.** The list is assembled from secondary compilations and is not exhaustive; the definition of "AI-discovered" varies by source. Before use in P7/P8, it must be rebuilt from registries (ClinicalTrials.gov/AACT, company filings) with a preregistered inclusion rule.
