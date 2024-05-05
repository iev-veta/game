#!/bin/bash
python3 -m venv breakout/.venv
source breakout/.venv/bin/activate
python3 setup.py sdist
pip3 install .
