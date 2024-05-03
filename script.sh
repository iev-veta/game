#!/bin/bash
source breakout/.venv/bin/activate
source breakout/.venv/Scripts/activate
source breakout/.venv\Scripts\activate
breakout/.venv/Scripts/activate
breakout/.venv\Scripts\activate
python3 setup.py sdist
pip3 install .
