# Runner Spec — Atomic/Molecular (H, He, H2) — v0.1

## Goals
1) Validate electron clouds (1s; 2s/2p) via occupancy histograms.
2) Demonstrate **partial sharing** in H2: non‑integer sharing fractions in bond region.

## Steps
- H: run `seed_H_atom.json`; export `orbital_density.csv` per schema.
- Drive weak periodic Θ to induce 2s/2p; capture spectral response.
- H2: run `seed_H2_molecule.json`; compute region occupancies; produce `shared_fraction(t)`.

## Acceptance
- H(1s): spherical density; 2s/2p nodal structure under drive.
- H2: sustained non‑zero shared_fraction in bond midplane; Θ_overlap minimized vs isolated H.
