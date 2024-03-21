#!/bin/bash

sudo apt update -y

sudo apt-get install -y python3-pip

cd /home/ubuntu || exit
git clone https://github.com/luisferico/thumbnail_gen.git

cd thumbnail_gen/streamlit_app || exit
sudo pip3 install -r requirements.txt

sudo nohup streamlit run main.py & disown
