# import re
import time
#
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(
#         user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
#     page = context.new_page()
#     page.goto("https://admin-test-v2.ccpayment.com/login")
#     with page.expect_popup() as page1_info:
#         page.get_by_role("button", name="icon-ic_auth_google Continue").click()
#     page1 = page1_info.value
#     page1.get_by_label("电子邮件地址或电话号码").click()
#     page1.get_by_label("电子邮件地址或电话号码").fill("jared0718@proton.me")
#     page1.get_by_role("button", name="下一步").click()
#     time.sleep(10)
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect

# def run(playwright: Playwright) -> None:
#     """
#     browser = p.chromium.connect_over_cdp("http://localhost:9999")
#     content = browser.contexts[0]
#     page = content.new_page()
#     """
#     # browser = playwright.chromium.connect_over_cdp("http://localhost:9999")
#     browser = playwright.webkit.launch(headless=False)
#     context = browser.new_context(
#         user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
#     # context = browser.new_context()
#     context.add_init_script(path='stealth.min.js')
#     page = context.new_page()
#     page.goto("https://admin-test-v2.ccpayment.com/login")
#     # page.goto("https://bot.sannysoft.com/")
#     with page.expect_popup() as page1_info:
#         page.get_by_role("button", name="icon-ic_auth_google Continue").click()
#     page1 = page1_info.value
#     page1.add_init_script(path='stealth.min.js')
#     page1.get_by_label("电子邮件地址或电话号码").click()
#     page1.get_by_label("电子邮件地址或电话号码").fill("jared0718@proton.me")
#     page1.get_by_role("button", name="下一步").click()
#     time.sleep(30)
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)


from playwright.sync_api import Playwright, sync_playwright
import subprocess

# 输入 Chrome 浏览器所在路径，并使用双引号将路径括起来
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
debugging_port = '--remote-debugging-port=9222'

# 使用列表形式表示命令及其参数
command = [chrome_path, debugging_port]
subprocess.Popen(command)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.connect_over_cdp('http://localhost:9222')
    context = browser.contexts[0]
    page = context.new_page()
    page.goto('baidu.com')


# 在这里调用 run() 函数
with sync_playwright() as playwright:
    run(playwright)
