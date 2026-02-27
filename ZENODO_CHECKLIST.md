
# Zenodo DOI Checklist (GitHub Integration)

1) Make the GitHub repository **public** and ensure **LICENSE** is present.
2) Add **CITATION.cff** (this file is provided here) to the repo root and customize as needed.
3) (Optional) Add **.zenodo.json** to control Zenodo metadata; if present, Zenodo prioritizes it over CITATION.cff.
4) Log in to **Zenodo** with GitHub and enable the repository under GitHub settings.
5) Create a **GitHub Release** (e.g., `v0.1-public`); Zenodo will archive it and mint a DOI.
6) After Zenodo minting, update **README.md** and **CITATION.cff** with the DOI badge.
