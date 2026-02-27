# Runner Spec — Nuclear (Deuteron) — v0.1

## Goals
Treat nuclear binding like chemical bonding: **partial sharing of loop orientation/anchor occupancy** in an overlap Θ well.

## Steps
- Run `seed_deuteron.json`; record `nuclear_coupling.csv` per schema.
- Track coupling_metric, net_winding_external, magnetic_moment_est.
- Scan distances to map binding window and unlocking threshold.

## Acceptance
- Phase‑lock plateau (non‑zero coupling_metric).
- Θ_overlap reduction vs separated loops.
- unlock_flag triggers beyond threshold; radiation bookkeeping (n=3 photons).
