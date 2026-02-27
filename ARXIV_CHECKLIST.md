
# arXiv Packaging Checklist (DEST)

- [ ] Rename main file to **Henkel_DEST_2026.tex** and place it at the top level of the submission ZIP (or in paper/ but compile from root accordingly).
- [ ] Ensure all file names use only allowed characters: a-z A-Z 0-9 _ + - . , = (no spaces).
- [ ] Figures: use **.pdf/.png/.jpg** if compiling with **pdflatex**; avoid mixing EPS with PDF/PNG/JPG.
- [ ] Bibliography: include **.bib** (BibTeX/Biber) _or_ the generated **.bbl** file.
- [ ] Include this **00README.arXiv** (optional but helpful for moderators).
- [ ] No external URLs for required figures; all assets included.
- [ ] Test a local compile with `pdflatex` twice (and BibTeX if used) before zipping.
- [ ] Zip from the submission root; avoid nested "/dest/dest/" paths.
