import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_httpd(url, timeout=120, interval=3):
    start = time.time()
    while True:
        try:
            r = requests.get(url, timeout=5, allow_redirects=False)
            if r.status_code in (200, 301, 302, 401, 403):
                print(f"HTTP is up. status={r.status_code}")
                return
            else:
                print(f"HTTP responded but not ready. status={r.status_code}")
        except requests.RequestException as e:
            print(f"HTTP not up yet: {e}")

        if time.time() - start > timeout:
            raise Exception("Timed out waiting for the HTTP server to start.")
        time.sleep(interval)

with open("/tmp/ip_address.txt", "r") as f:
    public_ip = f.read().strip()

target_url = f"http://{public_ip}/redmine"
wait_for_httpd(target_url)

options = Options()
options.add_argument("-headless")
options.set_preference("dom.ipc.processCount", 1)
options.set_preference("browser.tabs.remote.autostart", False)

driver = webdriver.Remote(
    command_executor=os.environ.get("SELENIUM_REMOTE_URL", "http://selenium:4444/wd/hub"),
    options=options
)

# Explicitly set timeouts to prevent hanging on low-resource (small) instances
driver.set_page_load_timeout(60)
driver.set_script_timeout(30)

driver.get(target_url)

wait = WebDriverWait(driver, 60)
# Use 'presence' instead of 'visibility' to avoid heavy rendering wait times
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.home")))

# Prioritize stability by using a standard window size instead of an oversized one
driver.set_window_rect(width=1365, height=768)

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshot.png")
driver.save_screenshot(filename)

driver.quit()
