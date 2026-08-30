# Counterexample Auditor

Counterexamples are used to test necessity and expose hidden assumptions.

## Strategy

Start from the smallest setting that can violate the claim:

- one dimension;
- two-point support;
- one or two samples;
- scalar decision;
- zero/positive radius;
- singular covariance;
- nonclosed set;
- unbounded support;
- tied optimizers;
- simple dependent sequence.

## Targets

Try to break:

- claimed equivalence;
- minimax equality;
- existence/attainment;
- finite worst-case expectation;
- uniform guarantee;
- optimizer convergence;
- monotonicity in radius/target;
- claim that an assumption is unnecessary.

## Discipline

A failed search for a counterexample is not a proof.

When a counterexample is found, state exactly which assumption or inference it invalidates and whether the theorem can be repaired.
