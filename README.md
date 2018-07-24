# RaspberryHomeCI
A home CI/CD built in python for the Raspberry Pi

The purpose is to install this repo into a Raspberry Pi 1b using Raspbian and Python 3.6.5, then use it as a CD/CI home server among other uses.
## Goals

 - [x] Mount Flask server to accept the web hook from Github/Bitbucket
 - [ ] Manage File System for cloning / pulling 
 - [ ] Send output to Slack Channel or Telegram
 - [ ] Refactor it!

## Installation

 1. Clone this repository
 2. Ensure python 3 is installed and type `pip install -r requirements.txt`
 3. Edit the server variables in the file `main.py`
 4. Run the server with `python3 main.py`

## Docker installation
The Dockerfile is on this repo if you want to check it out. It clones this repo and perform the install of the dependencies plus the execution of the flask server mapped with the 5000 port.
- `docker pull beruto/raspberry-home-ci`
 - `docker run --rm -p 5000:5000 --name=raspberry-home-pi -t raspberry-home-ci`