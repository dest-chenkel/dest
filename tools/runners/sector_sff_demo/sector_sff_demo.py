#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7)

N = 256                     # used only if we fall back to synthetic demo
beta = 0.5
sectors = ['NS_plus', 'NS_minus', 'R_minus']
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

def goe_spectrum(n):
    M = np.random.normal(0, 1, (n, n))
    M = (M + M.T) / 2.0
    evals = np.linalg.eigvalsh(M / np.sqrt(2 * n))
    return np.sort(evals)

def load_or_generate(label):
    """Try to load DEST energies from CSV; otherwise generate demo."""
    csv_path = os.path.join(output_dir, f'energies_{label}.csv')
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        if 'E' not in df.columns:
            raise ValueError(f"{csv_path} must contain a single column named 'E'.")
        E = df['E'].to_numpy().astype(float)
        E = np.sort(E)
        print(f"[{label}] Loaded {len(E)} energies from {csv_path}")
        return E, True
    else:
        # fallback: synthetic demo (with mild R-sector duplication)
        E = goe_spectrum(N)
        if label.startswith('R_'):
            E = np.sort(np.concatenate([E, E + np.random.normal(0, 1e-3, size=N)]))
        print(f"[{label}] Generated synthetic demo spectrum (size={len(E)})")
        # also write it out once so the file exists for transparency
        pd.DataFrame({'E': E}).to_csv(csv_path, index=False)
        return E, False

def sff(E, beta=0.5, t_grid=None):
    if t_grid is None:
        t_grid = np.linspace(0.0, 50.0, 400)
    E = E - np.min(E)    # numeric stability
    Z_2b = np.sum(np.exp(-2 * beta * E))
    K = []
    for t in t_grid:
        Z = np.sum(np.exp(-(beta + 1j*t) * E))
        K.append((np.abs(Z)**2) / Z_2b)
    return t_grid, np.array(K)

def main():
    all_curves = []
    for label in sectors:
        E, from_csv = load_or_generate(label)
        # Save back (sorted) so we see what was actually used
        pd.DataFrame({'E': E}).to_csv(os.path.join(output_dir, f'energies_{label}.csv'), index=False)

        t, K = sff(E, beta=beta)
        np.savez(os.path.join(output_dir, f'sff_{label}.npz'), t=t, K=K)

        plt.figure(figsize=(7, 4))
        plt.plot(t, K.real, lw=1.6)
        src = "DEST CSV" if from_csv else "demo"
        plt.title(f"SFF (beta={beta}) — {label}  [{src}]")
        plt.xlabel('t'); plt.ylabel('K_beta(t)')
        plt.grid(alpha=0.3); plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'sff_{label}.png'), dpi=160)
        plt.close()
        all_curves.append((label, t, K.real))

    plt.figure(figsize=(7.2, 4.5))
    for label, t, K in all_curves:
        plt.plot(t, K, lw=1.3, label=label)
    plt.title(f"SFF (beta={beta}) — per sector")
    plt.xlabel('t'); plt.ylabel('K_beta(t)')
    plt.legend(frameon=False); plt.grid(alpha=0.3); plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sff_combined.png'), dpi=180)
    plt.close()

if __name__ == "__main__":
    main()