import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# HTTPサーバーが起動していることを確認し、起動していなければ待機する関数
def wait_for_httpd(url, timeout=60):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("HTTPサーバーが起動しました。")
                break
        except requests.ConnectionError:
            print("HTTPサーバーがまだ起動していません。再試行します。")

        if time.time() - start_time > timeout:
            raise Exception("HTTPサーバーの起動を待機中にタイムアウトしました。")
        time.sleep(5)  # 5秒待機して再試行

# Reading the public IP address from /tmp/ip_address.txt
with open('/tmp/ip_address.txt', 'r') as file:
    public_ip = file.read().strip()

# Constructing the URL for Redmine
target_url = f"http://{public_ip}/redmine"

# HTTPサーバーが起動していることを確認
wait_for_httpd(target_url)

# Setting up headless Firefox options
options = Options()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Now that we've confirmed the server is up, we can proceed to access the page
driver.get(target_url)

# Wait for a specific element to be loaded
wait = WebDriverWait(driver, 60)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.home")))

w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_rect(width=w, height=h)

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./screenshot.png")

driver.save_screenshot(filename)

driver.quit()
