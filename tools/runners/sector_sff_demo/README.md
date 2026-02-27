# DEST Sector SFF Demo

This runner generates **sector‑tagged spectra** (NS_plus, NS_minus, R_minus) and computes
the **finite‑temperature spectral form factor**

\[ K_\beta(t) = |Z(\beta + i t)|^2 / Z(2\beta),\  Z(z)=\sum_j e^{-z E_j} \]

It’s a **demonstration** with GOE‑like ensembles (and a mild R‑sector degeneracy) to mirror
wormhole/RMT analyses in fermionic 3D gravity + 2D CFT.

## Run
```bash
python3 sector_sff_demo.py
```

Outputs are written to `output/`.
