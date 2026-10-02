# The Saka Law

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23092957.svg)](https://doi.org/10.5281/zenodo.23092957)

**A framework for measuring recursive technological acceleration and its implications for biomedical longevity**

Version 0.3.2 — 2 October 2026

This repository contains a conceptual forecasting paper developed around a proposed idea called the **Saka Law of Recursive Technological Acceleration**.

> **Status:** hypothesis / forecasting framework. It is not an established scientific law and it is not a claim that technological progress must remain exponential.

## Core idea

Technological progress can accelerate when technology begins to improve the process that produces new technology. In growth-economics terms, this is a claim about the feedback parameter of the idea-production function, set against evidence that research productivity has been falling for decades. The framework attempts to measure that feedback while explicitly accounting for bottlenecks, translation delays, evidence quality and accessibility.

The model combines:

- historical technology baselines;
- AI capability, compute and algorithmic efficiency;
- energy availability;
- robotics and autonomous laboratories;
- biotechnology maturity;
- measurement and biological data;
- manufacturing;
- space-enabled experimentation;
- clinical translation;
- bottlenecks, risks and diffusion.

The longevity component asks a narrower question: **can medical progress increase healthy-life expectancy fast enough to materially offset biological ageing?**

## Files

- [paper.md](./paper.md) — full conceptual paper.
- [model-spec.md](./model-spec.md) — equations, variables, proposed update procedure and candidate data sources (Section 13).
- [Saka_Law_v0.3.2.pdf](./Saka_Law_v0.3.2.pdf) — PDF of the paper with the specification as appendix.
- [forecasts/](./forecasts) — dated pre-commitments, e.g. how the ER-100 interim data (8 Oct 2026) will be read.
- [ai-attribution/](./ai-attribution) — calibration cases for the AI₀–AI₄ attribution scale.
- [LICENSE](./LICENSE) — CC BY 4.0.
- [CITATION.cff](./CITATION.cff) — citation metadata (used by GitHub and Zenodo).

## Suggested repository structure for future versions

```
saka-law/
├── README.md
├── paper.md
├── model-spec.md
├── data/
│   ├── historical_baseline.csv
│   ├── ai_metrics.csv
│   ├── biotech_translation.csv
│   └── energy_space_robotics.csv
├── notebooks/
│   ├── fit_growth_models.ipynb
│   └── monte_carlo_forecast.ipynb
└── figures/
```

## Citation

For now cite as:

**Carrasco, J. (Saka). (2026). _The Saka Law: Measuring Recursive Technological Acceleration and Its Implications for Biomedical Longevity_. Version 0.3.2. Zenodo. https://doi.org/10.5281/zenodo.23092958**

To cite the latest version instead of this specific one, use the concept DOI [10.5281/zenodo.23092957](https://doi.org/10.5281/zenodo.23092957).

## What changed in v0.3.2

- The hypothesis test (P2) now separates resource inputs (compute, energy, data, manufacturing) from capabilities, so an investment boom alone cannot count as acceleration.
- P4 now requires AI autonomy to *accelerate* (shorter doubling time), not just to keep growing exponentially.
- The longevity-escape-velocity proxy is normalized by the age gradient of healthy-life expectancy, making the period and individual definitions agree.
- Research productivity is measured against total research input including compute and automation.
- Multiple-comparison control and a power analysis are required before preregistration.

See the changelog at the end of [paper.md](./paper.md) for the full list.

## Important note

This version contains no numerical forecasts. Its weights and prediction thresholds are **subjective proposals**, not estimates or clinical predictions. Future versions should populate the component proxies with reproducible datasets, fix the thresholds in a preregistration, and add out-of-sample validation.

## License

The paper and specification are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): anyone may share and adapt them, including commercially, as long as they credit the author and indicate changes. See [LICENSE](./LICENSE).

Code added in future versions (data fetchers, notebooks) will be licensed separately under the MIT License, since Creative Commons licenses are not designed for software.
