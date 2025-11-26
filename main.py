#!/usr/bin/env python3
from dotenv import load_dotenv
from config.settings import HostCredentials
from services.reboot import reboot_device
from utils.ping import wait_for_host_ping3

def main():
    load_dotenv()
    config = HostCredentials.from_env(prefix="TPLINK_")
    for host in config.hosts:
        if wait_for_host_ping3(host):
            reboot_device(host, config.password, config.dry_run)

if __name__ == "__main__":
    main()
