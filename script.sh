#!/bin/bash
python -m venv breakout/.venv
source breakout/.venv/bin/activate
source breakout/.venv/Scripts/activate
python3 setup.py sdist
pip3 install .
