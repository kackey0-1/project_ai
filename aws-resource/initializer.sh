#!/usr/bin/env bash

echo "hello world!"
git clone https://github.com/kackey0-1/project_ai.git
cd project_ai
python3 --version

sudo apt update
sudo apt install -y python3-pip python3.8-venv python-celery-common
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

