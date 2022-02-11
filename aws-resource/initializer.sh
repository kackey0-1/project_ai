#!/usr/bin/env bash

git clone https://github.com/kackey0-1/project_ai.git
cd project_ai
python3 --version

sudo apt update
sudo apt install -y python3-pip python3-venv python-celery-common python3-h5py
sudo apt install -y docker docker-compose
#sudo usermod -aG docker ${USER}
#sudo su ${USER}
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

#sudo su
#source .venv/bin/activate
#flask run --host 0.0.0.0 --port 80
