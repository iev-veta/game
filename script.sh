#!/bin/bash
source .venv/bin/activate
source .venv/Scripts/activate
source .venv\Scripts\activate
.venv/Scripts/activate
.venv\Scripts\activate
python3 setup.py sdist
pip3 install .
