# Deviation-Regime Auditor

Statistical guarantees that look similar algebraically can live in fundamentally different asymptotic regimes. Classify the regime **before** interpreting a radius, confidence level, or rate.

## 1. Mandatory regime classification

For every statistical theorem, identify exactly one primary regime (and any secondary consequence):

1. **Non-asymptotic / finite-sample concentration**
   \[
   \mathbb P[\mathcal E_S]\ge 1-\delta_S
   \]
   for a stated finite sample size $S$, with no unquantified $o(1)$ remainder.

2. **Large deviations (LDP)**
   \[
   \limsup_{S\to\infty}\frac{1}{b_S}\log \mathbb P[\mathcal E_S^c]\le -r,
   \]
   usually with speed $b_S=S$. This controls the exponential decay **rate**, not the exact finite-$S$ probability.

3. **Moderate deviations (MDP)**
   An intermediate regime with a speed $b_S\to\infty$ that is sublinear relative to the large-deviation speed. Record the exact scaling used by the theorem.

4. **Central-limit / local asymptotic approximation**
   A normalized statistic converges in distribution to a Gaussian or another limiting law. This is not automatically a confidence guarantee at finite $S$.

5. **Law-of-large-numbers / consistency / almost-sure regime**
   The estimator, objective, set, or optimizer converges, but no decay rate or finite-sample confidence level is necessarily supplied.

## 2. No regime upgrading

The following upgrades are forbidden without an explicit theorem:

- LDP exponent -> finite-sample $1-\delta$ certificate;
- asymptotic normality -> exact confidence interval;
- almost-sure convergence -> finite-sample tail bound;
- MDP result -> LDP result;
- consistency -> convergence rate.

If an LDP gives
\[
\limsup_{S\to\infty}\frac1S\log \mathbb P[\mathcal E_S^c]\le-r,
\]
the valid interpretation is that the failure probability has asymptotic exponential rate at least $r$. Do **not** rewrite this as $\mathbb P[\mathcal E_S]\ge 1-e^{-rS}$ unless a non-asymptotic remainder inequality is proved.

## 3. LDP event topology

For an LDP with rate function $I$, separately check the two bounds:

- upper bound over the **closure** of an event;
- lower bound over the **interior** of an event.

A proof of optimality that needs a lower bound must establish that a suitable point lies in the event interior. A proof of feasibility using the upper bound must control the event closure. Do not silently replace either set by the event itself.

## 4. Speed and rate budget

Record:

- sample/time index $S$;
- LDP/MDP speed $b_S$;
- rate function $I$;
- rate budget $r$;
- event whose probability is controlled;
- whether the theorem is pointwise or uniform in the model/decision.

A parameter called a “radius” or “risk-aversion parameter” may encode a large-deviation **rate budget**, not a finite-sample metric radius. Interpret it according to the theorem that generated it.

## 5. Operational calibration

Ask whether a user can convert the asymptotic rate target into a finite-sample operating threshold. If the theorem gives only a limit superior/inferior, the calibration is asymptotic unless an explicit finite-$S$ correction is available.

## 6. Verdict language

Use language such as:

- **asymptotic exponential-rate guarantee**;
- **non-asymptotic finite-sample guarantee**;
- **moderate-deviation guarantee**;
- **asymptotic approximation**;
- **consistency only**.

Never use “finite-sample guarantee” as a generic synonym for “statistical guarantee.”
