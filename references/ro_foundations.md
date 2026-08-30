# RO Foundations for Research Use

## 1. Static RO

Generic robust constraint:

$$
f(\bm x,\bm z)\le 0 \qquad \forall \bm z\in\mathcal U.
$$

Key design choices:

- nominal point/center;
- uncertainty-set geometry;
- support bounds;
- uncertainty budget;
- correlations or coupled deviations;
- symmetric versus directional/asymmetric deviations.

The geometry is both a modeling assumption and a computational device.

## 2. Common uncertainty geometries

- box / interval;
- ellipsoid;
- polyhedron;
- budgeted norm set;
- general norm-induced coverage set;
- asymmetric/directional deviation set;
- learned/data-driven set;
- decision-dependent set.

Do not select a geometry only because it is solver-friendly. Explain why the uncertainty representation matches the primitive uncertainty.

## 3. Adjustable and multistage RO

When recourse decisions are made after partial information is observed, decisions are functions of the observation history. The central modeling requirement is nonanticipativity.

Approximation choices include:

- affine decision rules;
- segregated affine rules;
- piecewise rules;
- K-adaptability;
- finite partitions;
- exact dynamic formulations in special settings.

Every approximation must identify whether it restricts policy space and therefore produces a conservative bound.

## 4. Decision-dependent uncertainty versus information discovery

These concepts are distinct.

- Decision-dependent uncertainty set: decisions alter the possible realizations/distribution of uncertainty.
- Decision-dependent information discovery: decisions alter what is observed and when, changing the admissible recourse information structure.

Confusing them can change the nonanticipativity constraints and invalidate a model.

## 5. Robust satisficing/globalized/tolerated robustness

Target-based paradigms can endogenize robustness parameters or control degradation beyond a nominal/robust region. Treat these as alternative decision criteria, not as automatic relaxations of classical RO.

## 6. Data-driven uncertainty sets

When uncertainty-set parameters are estimated from data, distinguish:

- parameter estimation of center/scale/shape;
- calibration of coverage level;
- downstream robust feasibility/performance;
- finite-sample estimation error;
- invariance under changes of units/transformations.

A statistically meaningful data-driven set should state what population object it estimates and what guarantee survives finite data.
