# run_all.ps1: venv → install → DEST-toy energies → SFF → open plot
if (-Not (Test-Path .venv)) {
  python -m venv .venv
}
. .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install numpy pandas matplotlib

python .\dest_toy_generate_energies.py
python .\sector_sff_demo.py
Start-Process (Resolve-Path .\output\sff_combined.png)