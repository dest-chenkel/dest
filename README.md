# DEST — Discrete Electromagnetic Spacetime Theory

**DEST** (Discrete Electromagnetic Spacetime Theory) is a unified, mechanistic program in which observables emerge from a single action with **tick‑quantized local updates**, a scalar **Θ‑curvature** that acts as effective geometry, **integerized electromagnetic (EB) content** at the cell level, and a foundational **e/3 compositeness** postulate for electric content.

This repository contains the first public disclosure of DEST, including the initial paper source, figures, and project scaffolding.

---

## ✨ What’s new in this public release
- **Paper (first public draft):** Introduces the two core pillars, in reader‑impact order:  
  1) **e/3 compositeness** (conceptual leap; electron as a composite object),  
  2) **Discrete EB content** (the mechanistic substrate: integer EB counters and tick‑quantized updates).  
- **Repository structure** for future simulation tooling and artifacts.
- **Acknowledgments** highlight the value of modern science communicators.

---

## 📁 Repository structure
```
dest/
├─ assets/                  # shared images/diagrams for docs or site
├─ docs/                    # developer and design notes, API sketches, etc.
├─ paper/                   # LaTeX source for the DEST paper (first public release)
│  ├─ DEST_Paper.tex
│  └─ figures/              # figures used by the paper
├─ site/                    # future static site / docs build
├─ tools/                   # scripts and runners
├─ .gitattributes
├─ .gitignore
├─ LICENSE
└─ README.md
```

> Some folders are scaffolds for upcoming tools and documentation.

---

## 🧩 Key ideas
- **e/3 compositeness:** Uses \(e/3\) as the primitive electric quantum, enabling electron compositeness with a natural toroidal geometry.
- **Discrete EB content:** Electromagnetic content is stored in **integer EB counters**; updates occur in **quantized ticks**. Continuum EM emerges as a large‑scale approximation.
- **Θ‑curvature:** Measures expected actualize‑tick density per affine length; induces an effective geometry.

See the full argument in `paper/`.

---

## 📄 Building the paper
### Requirements
- A LaTeX distribution (TeX Live / MiKTeX) with common math/figure packages.

### Compile
```bash
pdflatex DEST_Paper_committed_order_singular_hill.tex
```
Use TeXstudio for an easier workflow.

---

## 🗺️ Roadmap
- Add simulation runners under `tools/`
- Add figure sets under `paper/figures/`
- Publish minimal documentation site from `site/`
- Tag the first public release branch

---

## 📚 Citation & Acknowledgments
If you reference DEST, please cite the repository and the LaTeX source in `paper/`.

**Acknowledgments** — I am grateful to the science communicators on YouTube and other open platforms who bring advanced ideas to broad audiences and help keep complex scientific concepts in active public conversation.

---

## 📝 License
See `LICENSE` at the repo root.

---

## 📬 Contact
- **Author:** Christopher Henkel  
- **Email:** christopher.henkel@gmail.com  
- **GitHub:** https://github.com/dest-chenkel/dest
