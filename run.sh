#!/bin/bash

# Install Python
sudo apt-get update
sudo apt-get install -y python3.9

# Init a new Python project
python3.9 -m venv venv
source venv/bin/activate

# Install Flask and sqlite3
pip install Flask sqlite3

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the Flask app
python app.py