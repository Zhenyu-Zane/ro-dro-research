# Oracle Quantity Auditor

A theorem can be correct while its advertised certificate is unusable. This auditor separates the two.

## Inventory every input

Create a table with:

`quantity | role | observable? | known by design? | estimable? | oracle? | bound/estimator supplied?`.

Typical oracle risks:

- $\mathbb P^\star$ itself;
- $\|\widehat{\bm\theta}-\bm\theta^\star\|$;
- unknown variance/tail proxy;
- unknown Lipschitz constant depending on the true model;
- unknown mixing time/coefficient;
- unknown support bound;
- unknown density lower bound;
- unknown true covariance/eigenvalue.

## Radius and tuning-parameter audit

For every ambiguity radius, uncertainty-set size, regularization coefficient, or confidence threshold, record:

`parameter | formula | data-observable inputs | unknown primitives | computable upper bound supplied? | confidence cost of estimating/bounding it | operational status`.

A rate can be theoretically explicit while still being non-operational because its constant depends on an unknown true moment or tail parameter. Keep these classifications separate.

## Classification

### Fully operational certificate

All required quantities are observed, known by design, or replaced by valid computable bounds whose confidence is included in the theorem.

### Data-driven with estimated nuisance quantities

Nuisance quantities are estimated and the theorem accounts for estimation error.

### Theoretical guarantee

The result is mathematically valid but contains unknown primitives.

### Oracle benchmark

The result assumes direct access to a true quantity for comparison or conceptual analysis.

## Veto rule

If a paper calls a result “computable,” “observable,” or an implementable finite-sample certificate while a required oracle quantity remains, return FAIL for that characterization even if the inequality itself is mathematically true.
