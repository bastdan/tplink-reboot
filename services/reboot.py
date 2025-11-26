from config.settings import HostCredentials
from playwright.sync_api import sync_playwright

def reboot_device(host, password, dry_run):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("http://" + host)
        page.fill("input[type='password']", password)
        page.wait_for_timeout(2000)
        page.click("a[title='LOG IN']")
        page.wait_for_url("**#networkMap")
        page.click('li[navi-value="advanced"] a')
        page.wait_for_url("**#networkStatus")
        page.click('li[navi-value="system"] a')
        if dry_run:
            print(f"[REBOOT] Dry run enabled. Skipping reboot command for {host}.")
            page.click('li[navi-value="reboot"] a')
        else:
            print(f"[REBOOT] Sending reboot command to {host}.")
            page.click('li[navi-value="reboot"] a')
        #page.pause()
        browser.close()