---
title: DEST Reading List
version: v0.1
description: A focused bibliography for building and communicating DEST—physics backbone, unification attempts, numerical methods, and writing/tooling references.
tags:
  - reading list
  - background
  - electromagnetism
  - relativity
  - quantum field theory
  - unification
  - numerical methods
  - documentation
---

# DEST Reading List — v0.1

A short, opinionated bibliography for DEST authors and contributors. The goal is to balance *foundational clarity* with *practical build-out* (mechanistic EM, Θ‑curvature correspondence, multi‑loop confinement/unlocking, orbitals/spectra, bonding, and numerical scaffolding).

---

## 0) Foundational Inspirations for DEST

- **“Is the Electron a Photon?” — YouTube (2026)**  
  A video discussion that motivated the search which ultimately led to the discovery of the Williamson & van der Mark (1997) toroidal‑photon paper—the conceptual seed that set the first domino falling in the eventual creation of DEST.  
  **URL:** https://youtu.be/f8O3XMrC8hg?si=DDXUnXuJq5jOdJpy
  
- **J.G. Williamson & M.B. van der Mark (1997) — *Is the electron a photon with toroidal topology?***  
  *Ann. Fond. Louis de Broglie* **22**(2), 133–160.  
  Early, semi‑classical program proposing that a **constrained photon with toroidal topology** can exhibit **charge, half‑integer spin, and a g‑factor near the electron’s**, seeded by **periodic boundary conditions at the Compton scale**. Resonates with DEST’s **3‑anchor loop**, **n‑class photons**, and **confinement/unlocking** ideas.  
  Archived in repo at: `assets/papers/williamson_vandermark_1997_electron_photon_toroidal.pdf`. [1]

---

## 1) Electromagnetism & Classical Foundations

- **D. J. Griffiths — *Introduction to Electrodynamics* (4th ed.)**  
  Clear Maxwell/fields pedagogy; useful for mapping DEST’s discrete EB counters and direction field to continuum checks.

- **J. D. Jackson — *Classical Electrodynamics* (3rd ed.)**  
  Reference-level EM; boundary conditions, radiation, and multipoles for validating DEST orbital/bonding fields.

- **H. Goldstein, C. Poole, J. Safko — *Classical Mechanics* (3rd ed.)**  
  Variational principles & symmetries; good scaffolding for DEST’s action-cost view (ΔS = h per local actualize).

---

## 2) Relativity & Geometry (for Θ → g^eff correspondence)

- **C. W. Misner, K. S. Thorne, J. A. Wheeler — *Gravitation***  
  Geodesics, lensing, Shapiro delay; use as the comparison set for DEST’s Θ‑induced effective geometry.

- **S. Carroll — *Spacetime and Geometry***  
  Compact GR reference; helpful when translating DEST ray-bending/redshift demos into standard GR language.

---

## 3) Quantum/Field‑Theory Intuition (beauty, symmetry, emergence)

- **R. P. Feynman — *QED: The Strange Theory of Light and Matter***  
  Intuition for light–matter interactions; good language for explaining DEST’s n‑class photons to non‑experts.

- **M. E. Peskin, D. V. Schroeder — *An Introduction to Quantum Field Theory***  
  Use for terminology alignment and to position DEST’s “no extra fields” stance vs. conventional QFT.

- **P. A. M. Dirac — *The Principles of Quantum Mechanics***  
  Concision and mathematical beauty; background for DEST’s elegance claims.

---

## 4) Unification Attempts & Big‑Picture Context

- **S. Weinberg — *Dreams of a Final Theory***  
  Philosophical/technical arguments for unification and what “beauty” buys you in theory-building.

- **G. ’t Hooft (essays/lectures on locality and determinism)**  
  Useful counterpoints on locality/hidden variables; helps sharpen DEST’s drift/actualize locality.

- **E. Witten (selected reviews on gauge/string unification)**  
  High‑end math/physics language to benchmark where DEST diverges (no additional fields) yet seeks unified phenomenology.

---

## 5) Atoms, Spectra, and Bonds (mechanistic targets)

- **B. H. Bransden, C. J. Joachain — *Physics of Atoms and Molecules***  
  Spectra, selection rules, molecular bonding—invaluable for checking DEST’s Δ(mode) line predictions and partial‑sharing bonds.

- **P. W. Atkins, R. Friedman — *Molecular Quantum Mechanics***  
  Electronic structure and bonding explained cleanly; good to translate DEST’s 3‑anchor occupancy into chemistry‑friendly terms.

- **I. N. Levine — *Quantum Chemistry***  
  Benchmarks for orbital densities, term symbols, and bond orders against DEST’s shared_fraction & Θ_overlap metrics.

---

## 6) Nuclear Structure & Phenomena (strong/weak analogues)

- **R. Machleidt, I. Towner (reviews on deuteron & nuclear forces)**  
  Deuteron binding windows and plateaus you can echo with DEST coupling_metric scans.

- **K. S. Krane — *Introductory Nuclear Physics***  
  Useful for neutron β‑decay phenomenology (DEST’s unlocking + n=1 packet bookkeeping).

---

## 7) Discrete/Geometric Numerics (for DEC‑style backbone)

- **E. Hairer, G. Wanner — *Solving Ordinary Differential Equations II* (Geometric Integrators)**  
  Structure-preserving numerics; helps avoid drift in conserved quantities in DEST runners.

- **A. N. Hirani — *Discrete Exterior Calculus* (thesis) & related papers**  
  Incidence/Hodge operators and d²=0 identities—parallel the tests you plan (Faraday/continuity, residual dashboards).

- **T. Levi-Civita, *The Absolute Differential Calculus* (historical)**  
  Classical reference when translating Θ‑curvature discussions into metric‑like language.

---

## 8) Complexity, Info & Thermo Intuition

- **I. Prigogine — *From Being to Becoming***  
  Irreversibility and emergent order—context for DEST’s S_info vs. S_geo story.

- **E. T. Jaynes — *Probability Theory: The Logic of Science***  
  Entropic reasoning; helpful language for directional vs. geometric entropies.

---

## 9) Writing, LaTeX, and Docs Tooling

- **L. Lamport — *LaTeX: A Document Preparation System***  
  For consistent paper builds (your `DEST_Paper.tex` pathway).

- **MkDocs Material (online docs)**  
  Clean site generation for your `site/mkdocs.yml` structure; supports tags and nice navigation.

---

## 10) DEST‑adjacent Inspirations (short reads / essays)

- **F. Wilczek — essays on symmetry & beauty**  
  Bridges the aesthetics → physics link that DEST emphasizes.

- **R. Feynman — “The Character of Physical Law” (lectures)**  
  Storytelling techniques for the public DEST narrative.

---

## Using this List

- Start with **Griffiths** (EM), **Carroll** (GR), **Bransden & Joachain** (spectra/bonds), and **Hirani** (DEC).  
- When drafting paper sections, sprinkle language inspired by **Dirac**, **Weinberg**, and **Feynman** to keep it clean and compelling.  
- When implementing runners/telemetry, keep **Hairer & Wanner** close for structure‑preserving steps and stability checks.