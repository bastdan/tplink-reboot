# TP-Link Reboot Automation

This is a basic automation for rebooting domestic TP-Link routers.

## Getting started

1. Dependencies:
* Install Python 3.10
* Allow for all users to ping remote hosts: `sudo sysctl -w net.ipv4.ping_group_range="0 2147483647"`

2. Copy env.template and fill out values.
3. Create the venv: `python -m venv .venv`
4. Activate the venv: `source ./venv/bin/activate`
5. Install project dependencies: `pip install -r requirements.txt`
6. Run `python main.py`