#!/bin/sh
eval "$(conda shell.bash hook)"
conda activate ml

python3 -m pip install -U so_ml_tools --no-deps
