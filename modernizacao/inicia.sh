#!/bin/bash

source .venv/bin/activate
export FLASK_APP=run.py
flask db upgrade
flask seed
python run.py
