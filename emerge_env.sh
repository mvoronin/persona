#!/bin/bash

PYTHON="python3.10"

sudo apt-get install python3-venv

$PYTHON -m venv env

source ./env/bin/activate

pip install -r requirements.txt
