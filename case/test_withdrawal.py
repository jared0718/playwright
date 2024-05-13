import time
import pytest
from playwright.sync_api import sync_playwright, expect
import subprocess


@pytest.fixture(scope="class")
def setup_fixture(request):
    # chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    chrome_path = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
    debugging_port = '--remote-debugging-port=9222'
    user_data_dir = '--user-data-dir=/Users/jaylan/PycharmProjects/PlaywrightUiTest/chrome_cache'
    # user_data_dir = '--user-data-dir=/chrome_cache'
    command = [chrome_path, debugging_port, user_data_dir]
    # subprocess.Popen(command)
    process = subprocess.Popen(command)
    playwright = sync_playwright().start()
    # 连接已打开浏览器，找好端口
    browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:9222")
    default_context = browser.contexts[0]  # 注意这里不是browser.new_page()了
    default_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = default_context.pages[0]

    # page.goto("https://admin-test-v2.ccpayment.com/dashboard/index")

    # def close_browser():
    #     browser.close()
    #     process.terminate()
    # def setup():
    #     nonlocal default_context
    #     # context = browser.new_context()
    #     # page = context.new_page()
    #     default_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #     page = default_context.pages[0]
    #     page.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
    #
    #     # 启用跟踪功能并设置相关配置
    #     default_context.tracing.start(screenshots=True, snapshots=True)
    #
    #     return page

    def teardown():
        page.close()
        browser.close()
        process.terminate()  # 关闭浏览器进程

    request.addfinalizer(teardown)
    return page


@pytest.mark.usefixtures("setup_fixture")
class TestTrade:

    # def test_withdrawal_to_network(self, setup_fixture):
    #     """
    #     上链 TETH
    #     """
    #     # time.sleep(60)
    #     setup_fixture.get_by_role("button", name="Balance").click()
    #     setup_fixture.get_by_role("row", name="logo TETH").get_by_role("button").nth(1).click()
    #     setup_fixture.get_by_label("Enter Address").click()
    #     setup_fixture.get_by_label("Enter Address").fill("0x12438F04093EBc87f0Ba629bbe93F2451711d967")
    #     setup_fixture.get_by_label("Amount").click()
    #     setup_fixture.get_by_label("Amount").fill("0.002")
    #     setup_fixture.get_by_role("button", name="Send").click()
    #     # time.sleep(2)
    #     setup_fixture.get_by_label("Payment Password").click()
    #     setup_fixture.get_by_label("Payment Password").fill("111111")
    #     setup_fixture.get_by_label("Email Verification Code").click()
    #     setup_fixture.get_by_label("Email Verification Code").fill("123456")
    #     setup_fixture.get_by_role("button", name="Confirm").click()
    #     time.sleep(5)
    #     setup_fixture.get_by_label("close").click()
    #
    # def test_withdrawal_to_merchant(self, setup_fixture):
    #     """
    #     同一账号商户转商户(内部)
    #     """
    #     time.sleep(3)
    #     setup_fixture.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
    #     setup_fixture.get_by_role("button", name="Balance").click()
    #     setup_fixture.get_by_role("row", name="logo TETH").get_by_role("button").nth(1).click()
    #     setup_fixture.get_by_label("Enter Address").click()
    #     setup_fixture.get_by_label("Enter Address").fill("0x390744104E2dbe47B48D336Fa8EaA937df435962")
    #     setup_fixture.get_by_label("Amount").click()
    #     setup_fixture.get_by_label("Amount").fill("0.002")
    #     setup_fixture.get_by_role("button", name="Send").click()
    #     # time.sleep(2)
    #     setup_fixture.get_by_label("Payment Password").click()
    #     setup_fixture.get_by_label("Payment Password").fill("111111")
    #     setup_fixture.get_by_label("Email Verification Code").click()
    #     setup_fixture.get_by_label("Email Verification Code").fill("123456")
    #     setup_fixture.get_by_role("button", name="Confirm").click()
    #     time.sleep(5)
    #     expect(setup_fixture.get_by_text("Transaction successful !")).to_contain_text('Transaction successful !')
    #     setup_fixture.get_by_label("close").click()
    #
    # def test_withdrawal_to_cwalletID(self, setup_fixture):
    #     """
    #     通过cwallet ID 转账(内部)
    #     """
    #     time.sleep(3)
    #     setup_fixture.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
    #     setup_fixture.get_by_role("button", name="Balance").click()
    #     setup_fixture.get_by_role("row", name="logo DOGE").get_by_role("button").nth(1).click()
    #     setup_fixture.get_by_label("To Cwallet ID").check()
    #     setup_fixture.get_by_role("textbox", name="To Cwallet ID").click()
    #     setup_fixture.get_by_role("textbox", name="To Cwallet ID").fill("9558861")
    #     setup_fixture.get_by_label("Amount").click()
    #     setup_fixture.get_by_label("Amount").fill("0.002")
    #     setup_fixture.get_by_role("button", name="Send").click()
    #     # time.sleep(2)
    #     setup_fixture.get_by_label("Payment Password").click()
    #     setup_fixture.get_by_label("Payment Password").fill("111111")
    #     setup_fixture.get_by_label("Email Verification Code").click()
    #     setup_fixture.get_by_label("Email Verification Code").fill("123456")
    #     setup_fixture.get_by_role("button", name="Confirm").click()
    #     time.sleep(5)
    #     expect(setup_fixture.get_by_text("Transaction successful !")).to_contain_text('Transaction successful !')
    #     setup_fixture.get_by_label("close").click()

    def test_withdrawal_to_cwallet_address(self, setup_fixture):
        """
        通过cwallet address 转账(内部)
        """
        time.sleep(3)
        setup_fixture.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
        setup_fixture.get_by_role("button", name="Balance").click()
        setup_fixture.get_by_role("row", name="logo DOGE").get_by_role("button").nth(1).click()
        setup_fixture.get_by_label("Enter Address").click()
        setup_fixture.get_by_label("Enter Address").fill("D5JZrM2UPWZ6uf7o6wzBKzGXQ9fUcPiVNi")
        setup_fixture.get_by_role("combobox").click()
        setup_fixture.get_by_role("option", name="Dogecoin").click()
        setup_fixture.get_by_label("Amount").click()
        setup_fixture.get_by_label("Amount").fill("0.02")
        setup_fixture.get_by_role("button", name="Send").click()
        # time.sleep(2)
        setup_fixture.get_by_label("Payment Password").click()
        setup_fixture.get_by_label("Payment Password").fill("111111")
        setup_fixture.get_by_label("Email Verification Code").click()
        setup_fixture.get_by_label("Email Verification Code").fill("123456")
        setup_fixture.get_by_role("button", name="Confirm").click()
        time.sleep(5)
        expect(setup_fixture.get_by_text("Transaction successful !")).to_contain_text('Transaction successful !')
        setup_fixture.get_by_label("close").click()
