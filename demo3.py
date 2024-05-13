import time
import subprocess
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch_persistent_context(
        # 指定本机用户缓存地址
        user_data_dir='chrome_cache',
        # 指定本机google客户端exe的路径
        executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        # 要想通过这个下载文件这个必然要开  默认是False
        accept_downloads=True,
        # 设置不是无头模式
        headless=False,
        bypass_csp=True,
        slow_mo=10,
        # 跳过检测
        args=['--disable-blink-features=AutomationControlled', '--remote-debugging-port=9222']
    )
    page = browser.new_page()
    page.goto("https://console.ccpayment.com/balances/index")
    # time.sleep(1000)
    page.get_by_role("row", name="logo TETH").get_by_role("button").nth(1).click()
    page.get_by_label("Enter Address").click()
    page.get_by_label("Enter Address").fill("0x12438F04093EBc87f0Ba629bbe93F2451711d967")
    page.get_by_label("Amount").click()
    page.get_by_label("Amount").fill("0.002")
    page.get_by_role("button", name="Send").click()
    page.get_by_label("Payment Password").click()
    page.get_by_label("Payment Password").fill("111111")
    page.get_by_role("button", name="Confirm").click()
    time.sleep(2)
    page.get_by_label("close").click()
    # print(page.title())
    time.sleep(200)
    browser.close()
