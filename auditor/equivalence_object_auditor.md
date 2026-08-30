# Equivalence Object Auditor

A statement that two models “coincide,” “are equivalent,” or “reduce to the same problem” is incomplete until the object of equivalence is named.

## 1. Identify the object being compared

For each equivalence claim, classify it as one or more of:

- equality of the original uncertainty/ambiguity sets;
- equality of projected or induced uncertainty/ambiguity sets;
- equality of feasible decision sets;
- equality of objective functions pointwise in the decision;
- equality of optimal values;
- equality of optimizer sets;
- existence of a map from optimizers of one model to optimizers of the other;
- equality only for a restricted decision class, loss class, risk measure, or information structure.

Do not promote a weaker object into a stronger one. In particular, equality of projected ambiguity sets can make two decision problems identical for a specified decision class even when the original ambiguity sets are different.

## 2. Quantify the scope

Write the claim in the form

`For every [decision / loss / risk criterion] in [class], object A equals object B under [conditions].`

If the result only holds after applying a projection, affine rule, sufficient statistic, recourse restriction, or other map, display that map explicitly.

## 3. Check set-level versus value-level language

The following implications are invalid without additional proof:

- same optimal value => same feasible set;
- same optimal value => same optimizer set;
- same projected set => same original set;
- same worst-case value for one loss => same ambiguity set;
- same model for affine rules => same model for nonlinear rules.

## 4. Counterfactual check

Ask whether the claimed equivalence survives when the decision class is enlarged or the projection is removed. If not, the qualifier is essential and must appear in the final statement.

## 5. Verdict rule

Return **PASS** only when the exact object and scope of equivalence are proved. If the mathematics is correct but the prose overstates the object being equated, return **PASS WITH EXPLICIT CONDITIONS** and rewrite the claim at the correct granularity.
