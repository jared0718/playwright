import time
import subprocess
from playwright.sync_api import sync_playwright

# chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_path = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
debugging_port = '--remote-debugging-port=9222'
user_data_dir = '--user-data-dir=/Users/jaylan/PycharmProjects/PlaywrightUiTest/chrome_cache'
command = [chrome_path, debugging_port, user_data_dir]
subprocess.Popen(command)
# time.sleep(5)

playwright = sync_playwright().start()
# 连接已打开浏览器，找好端口
browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:9222")
default_context = browser.contexts[0]  # 注意这里不是browser.new_page()了
page = default_context.pages[0]
page.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
# time.sleep(30000)
page.get_by_role("button", name="Balance").click()
# page.get_by_role("button", name="icon-banlanceCloseEye").click()
# page.get_by_text("row", name="logo TETH 0.49022475 0.00 USD").get_by_role("button").nth(1).click()
page.get_by_role("row", name="logo TETH ****** ****** 0.00").get_by_role("button").nth(1).click()
page.get_by_label("Enter Address").click()
page.get_by_label("Enter Address").fill("0x12438F04093EBc87f0Ba629bbe93F2451711d967")
page.get_by_label("Amount").click()
page.get_by_label("Amount").fill("0.002")
page.get_by_role("button", name="Send").click()
page.get_by_label("Payment Password").click()
page.get_by_label("Payment Password").fill("111111")
page.get_by_label("Email Verification Code").click()
page.get_by_label("Email Verification Code").fill("123456")
page.get_by_role("button", name="icon-gray_close_eye").click()
page.get_by_role("button", name="Confirm").click()
time.sleep(5)
page.get_by_label("close").click()
