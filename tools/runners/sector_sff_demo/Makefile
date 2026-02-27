# Makefile: venv → install → run → open (POSIX/Git Bash)
PY=python3
VENV=.venv
BIN=$(VENV)/bin
PIP=$(BIN)/pip
PYTHON=$(BIN)/python

.PHONY: all venv install run open clean

all: run open

venv:
    $(PY) -m venv $(VENV)

install: venv
    $(PIP) install --upgrade pip
    $(PIP) install numpy pandas matplotlib

run:
    $(PYTHON) sector_sff_demo.py

open:
    @echo "Opening combined SFF plot…"
    @$(PYTHON) -c "import webbrowser; webbrowser.open('file://' + __import__('os').path.abspath('output/sff_combined.png'))"

clean:
    rm -rf $(VENV) output/*.npz output/*.png output/*.csv