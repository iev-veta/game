#!/bin/bash
source .venv/bin/activate
python3 setup.py sdist
pip3 install .