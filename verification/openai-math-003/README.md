# Independent checks: OpenAI family 003, "The Quasi-Riemann Hypothesis"

**Paper checked:** *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane ℜs > 7/8*, OpenAI, 30 September 2026, 199 pages, in [github.com/openai/math](https://github.com/openai/math) (`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf`, upstream commit `adc7f1241`).

**Claim:** every Dirichlet L-function, including ζ(s), and every finite-order Hecke L-function over ℚ(√−3) has no zero with ℜs > 7/8 (principal pole at s = 1 allowed).

**Checked on:** 7 October 2026. **By:** a Claude model (Anthropic), working with the repository maintainer. Conflict of interest: the paper was produced by a competitor's model.

**What this is and is not.** These are partial, independent consistency checks of parts of the paper that can be tested exactly or numerically. They are **not** a verification of the theorem. The deep estimates in Sections 5–19 (character large sieves, the zero detector, the inductive moment bounds) are asymptotic inequalities with implied constants and cannot be tested this way. A full check requires expert review or the complete Lean/Comparator verification (see the `isaksmith/math` fork for a statement-fidelity review and a local build).

## 1. Structure of the proof (reading notes)

- **Family.** The argument works with all finite-order Hecke L-functions over ℚ(√−3), because its Poisson representation produces Hecke twists of the target. Dirichlet L-functions and ζ are reached at the end by factorization (Section 11.2).
- **Continuation principle (Proposition 2.1).** Let β* be the supremum of real parts of zeros in the family. Assuming β* > σ₀, for each target a character sum J(Z) is (a) bounded directly and (b) compared with a Mellin integral containing 1/L. Power savings in both, uniform in the target, continue 1/L to the left of β*, a contradiction. *Checked by hand: the argument is sound.*
- **The sum.** Smoothed Fourier coefficients of Patterson's cubic theta series, averaged against sextic residue characters. It has two exact representations: a cubic-theta reflection (Section 5) and Poisson summation (Section 7), whose principal row contains 1/L.
- **Part I** gives ℜs > 11/12 (Section 11). **Part II** adds prime compensation, asymmetric scales and two inductive moment estimates (Sections 17–18, about 65 pages) to reach 7/8.
- **Most delicate step.** The non-principal Poisson rows involve L-functions of twists, which may themselves have zeros up to β*. The proof needs their total contribution to stay below the principal signal by a target-independent power. This is done with a zero detector (Section 8) and sextic large-sieve row counts (Sections 9, 19) fed by the moment inductions. If the proof has an error, it is most likely here.
- **Margin.** The final bookkeeping (Lemma 20.2) closes with a very small margin: −E* ≥ 49/440640 ≈ 1.1 × 10⁻⁴.
- **Consequence stated in the paper (Corollary 1.2).** Vinogradov's least quadratic nonresidue conjecture, n(p) ≤ C(log p)^A, and a deterministic polynomial-time algorithm for square roots modulo a prime — previously known only under GRH-type hypotheses.

## 2. Exact check of the Section 20 bookkeeping — `check_section20.py`

All exponent arithmetic in Section 20 checked with exact rational arithmetic (SymPy): the geometry (h, ℓ, lₓ, l_y), the two lines of Equation (20.4), Equations (20.5)–(20.7) and (20.11), the frequency-range inequalities of Section 20.5, the margins m_w, m_z, m_hi, κ_P, and Lemma 20.2 in full — the formula for J, the expression for −E*, the quadratic in δ, the completion-of-the-square identity (20.9), and the lower bound 49/440640 (also confirmed on a 41 × 41 grid; the grid minimum is 7/28608 ≈ 2.4 × 10⁻⁴).

**Result: 34/34 checks pass** (`output_section20.txt`). The inputs D_x, P_x, R_short, L(t) are taken from Proposition 19.2 as stated; that proposition itself is not checked.

## 3. Numerical check of Lemmas 4.2–4.4 — `check_section4.py`

Exact arithmetic in ℤ[ω] for 35 primary primes (split primes up to 139, inert primes up to 37; norms up to 841) and squarefree composites: prime Gauss sum identities (Lemma 4.2), the quadratic four-term formula, its unit table and bicharacter (Lemma 4.3, on 300 random odd elements), sextic reciprocity χ_b(a) = R(a,b)χ_a(b) for prime and composite pairs, the multiplicativity of G and the squarefree Gauss identities (4.5)–(4.7) (Lemma 4.4).

**Result: all 16 identity families pass, 1,573 individual comparisons** (`output_section4.txt`).

Note: a first run failed on γ₁γ₂ = H(4)γ₃γ₂³. The cause was our text extraction, which dropped conjugation bars; the PDF reads $\overline{H(4)}$ and $G(c)=\overline{\chi_c(4)}\Gamma(c)$. With the bars, every check passes.

## 4. What remains

- Sections 5–19: expert review, or the clean-room Comparator run of the Lean formalization.
- The Hecke statement over ℚ(√−3) defines its own L-function machinery in Lean; its statement fidelity needs a manual check.
- The Siegel-zero companion paper (family 003, second formalized paper) states a non-explicit constant; whether it is effective is not addressed here.

## Reproduce

```bash
pip install sympy
python3 check_section20.py     # seconds
python3 check_section4.py      # about 40 s
```
