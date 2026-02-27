# run.ps1: venv → install → run → open (PowerShell)
if (-Not (Test-Path .venv)) {
  python -m venv .venv
}
. .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install numpy pandas matplotlib
python .\sector_sff_demo.py
Start-Process (Resolve-Path .\output\sff_combined.png)