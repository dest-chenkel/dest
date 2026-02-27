#!/usr/bin/env python3
"""
dest_toy_generate_energies.py
--------------------------------
A tiny, reproducible "DEST‑toy" surrogate that produces sector-tagged energies
(NS_plus, NS_minus, R_minus) so the SFF pipeline can be run end-to-end.

WHAT IT DOES (surrogate, not physics):
  * Creates a small 2D 'EB' state on an LxL lattice.
  * Evolves it for T time steps with a simple local rule (diffusion + nonlinearity).
  * Uses three different boundary toggles to emulate sectoring:
      - NS_plus   : antiperiodic in x, periodic in y  (toy)
      - NS_minus  : periodic in x, antiperiodic in y  (toy)
      - R_minus   : periodic in both (toy), plus mild two-block pairing
  * Collects a time window of flattened states per sector -> builds a covariance
    operator C ~ X^T X / (T-1), diagonalizes C, and writes eigenvalues as 'energies'.

OUTPUT:
  dest/tools/runners/sector_sff_demo/output/energies_NS_plus.csv
  dest/tools/runners/sector_sff_demo/output/energies_NS_minus.csv
  dest/tools/runners/sector_sff_demo/output/energies_R_minus.csv
"""
import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(17)

OUT = Path(__file__).parent / "output"
OUT.mkdir(parents=True, exist_ok=True)

# --- Toy lattice parameters
L = 32                  # lattice size L x L
T_total = 180           # total steps
T_win   = 96            # last T_win frames -> spectrum
alpha   = 0.35          # diffusion weight
beta    = 0.015         # pointwise nonlinearity

def step(EB, bc):
    """
    One toy update: discrete diffusion + tiny nonlinearity.
    Boundary conditions:
      bc='px_py'  : periodic x, periodic y
      bc='ax_py'  : antiperiodic x, periodic y
      bc='px_ay'  : periodic x, antiperiodic y
    """
    Lx, Ly = EB.shape
    def shift_x(a, k):
        if bc in ('px_py', 'px_ay'):
            return np.roll(a, k, axis=1)
        elif bc in ('ax_py',):
            # antiperiodic in x: roll + sign flip at wrap
            s = np.roll(a, k, axis=1).copy()
            if k > 0:
                s[:, :k] *= -1.0
            elif k < 0:
                s[:, k:] *= -1.0
            return s
        else:
            # default fallback
            return np.roll(a, k, axis=1)

    def shift_y(a, k):
        if bc in ('px_py', 'ax_py'):
            return np.roll(a, k, axis=0)
        elif bc in ('px_ay',):
            # antiperiodic in y
            s = np.roll(a, k, axis=0).copy()
            if k > 0:
                s[:k, :] *= -1.0
            elif k < 0:
                s[k:, :] *= -1.0
            return s
        else:
            return np.roll(a, k, axis=0)

    lap = (shift_x(EB,1) + shift_x(EB,-1) + shift_y(EB,1) + shift_y(EB,-1) - 4*EB)
    EB = EB + alpha * lap - beta * np.tanh(EB)
    return EB

def run_sector(bc, seed=0):
    """
    Run the toy evolution under chosen boundary toggle, collect last T_win frames
    as flattened vectors, form covariance spectrum as 'energies'.
    """
    rng = np.random.default_rng(seed)
    EB = rng.normal(0, 0.5, (L, L))

    frames = []
    for t in range(T_total):
        EB = step(EB, bc)
        if t >= T_total - T_win:
            frames.append(EB.ravel())

    X = np.stack(frames, axis=0)               # T_win x (L*L)
    X = X - X.mean(axis=0, keepdims=True)      # center
    C = (X.T @ X) / max(1, (X.shape[0] - 1))   # covariance operator
    # symmetric safety
    C = 0.5 * (C + C.T)
    E = np.linalg.eigvalsh(C)
    E = np.sort(E.real.astype(float))
    return E

def write_csv(E, name):
    pd.DataFrame({'E': E}).to_csv(OUT / f"energies_{name}.csv", index=False)
    print(f"[OK] wrote {len(E)} energies -> {OUT / f'energies_{name}.csv'}")

def main():
    # Map toy BCs to sector names
    #  NS+ : antiperiodic x, periodic y
    #  NS- : periodic x,   antiperiodic y
    #  R-  : periodic x,   periodic y
    E_ns_plus  = run_sector(bc='ax_py', seed=11)
    E_ns_minus = run_sector(bc='px_ay', seed=13)
    E_r_minus  = run_sector(bc='px_py', seed=17)

    # Optional: emulate mild two-block structure in R- by duplicating with jitter
    jitter = np.random.normal(0, 1e-6, size=E_r_minus.shape)
    E_r_minus = np.sort(np.concatenate([E_r_minus, E_r_minus + jitter]))

    write_csv(E_ns_plus,  "NS_plus")
    write_csv(E_ns_minus, "NS_minus")
    write_csv(E_r_minus,  "R_minus")

if __name__ == "__main__":
    main()