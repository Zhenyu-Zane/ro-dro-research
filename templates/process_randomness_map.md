# Process Randomness Map

Use for trajectory/time-series/Markov/autoregressive data.

```text
process parameter theta*
        |
        v
infinite process law P_{theta*}
        |
        +--> finite path law P_{theta*}^{(S)}
                  |
                  v
          training trajectory xi_[S]
                  |
                  v
          statistic S_hat_S
                  |
        +---------+----------+
        |                    |
        v                    v
parameter/process        ambiguity set
estimator                {theta: I(S_hat_S,theta)<=r}
                              |
                              v
                       data-driven decision
                              |
                              v
                       future/test risk
```

Fill in process state space; parameter space and closure; stationarity/ergodicity/mixing assumptions; initialization law; one trajectory vs independent trajectories; finite-horizon path law; statistic and limiting value; LDP/concentration theorem and rate function; ambiguity-set object; future/test relationship to training process; and downstream decision risk.
