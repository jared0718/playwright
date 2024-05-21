import time
import pytest
from playwright.sync_api import sync_playwright, expect
import subprocess

"""
CCPayment商户后台提现相关：自动化脚本
1. 上链 TETH
2. 同一账号商户转商户(内部)
3. 通过cwallet ID 转账(内部)
4. 通过cwallet address 转账(内部)

说明：
1. 商户后台系统 登录部分
无法通过接口(拿Token)或自动化(1.邮箱登录人机验证过不了； 2.谷歌登录谷歌检测 自动化操作 不安全)操作登录
所以只有在执行自动化操作前 手动登录，再打开同一个浏览器进程保持登录状态 来进行操作

常用命令：
1. Generating tests：
playwright codegen < url >
2. Trace viewer
生成：pytest --tracing on
打开报告：playwright show-trace trace.zip
3. 普通运行项目
pytest
"""


@pytest.fixture(scope="class")
def setup_fixture(request):
    # chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' # 用Chrome浏览器
    chrome_path = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'  # 用Edge浏览器
    debugging_port = '--remote-debugging-port=9222'
    user_data_dir = '--user-data-dir=/Users/jaylan/PycharmProjects/PlaywrightUiTest/chrome_cache'
    command = [chrome_path, debugging_port, user_data_dir]
    process = subprocess.Popen(command)
    playwright = sync_playwright().start()
    browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:9222")
    default_context = browser.contexts[0]
    # default_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = default_context.pages[0]

    def teardown():
        # default_context.tracing.stop(path='trace.zip')
        page.close()
        browser.close()
        process.terminate()

    request.addfinalizer(teardown)
    return page


@pytest.mark.usefixtures("setup_fixture")
class TestTrade:

    def test_withdrawal_to_network(self, setup_fixture):
        """
        上链 TETH
        """
        setup_fixture.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
        setup_fixture.get_by_role("button", name="Balance").click()
        setup_fixture.get_by_role("row", name="logo TETH").get_by_role("button").nth(1).click()
        setup_fixture.get_by_label("Enter Address").click()
        setup_fixture.get_by_label("Enter Address").fill("0x12438F04093EBc87f0Ba629bbe93F2451711d967")
        setup_fixture.get_by_label("Amount").click()
        setup_fixture.get_by_label("Amount").fill("0.002")
        setup_fixture.get_by_role("button", name="Send").click()
        setup_fixture.get_by_label("Payment Password").click()
        setup_fixture.get_by_label("Payment Password").fill("111111")
        setup_fixture.get_by_label("Email Verification Code").click()
        setup_fixture.get_by_label("Email Verification Code").fill("123456")
        setup_fixture.get_by_role("button", name="Confirm").click()
        time.sleep(5)
        expect(setup_fixture.get_by_role("heading", name="Transaction Detail close")).to_contain_text(
            'Transaction Detail')
        setup_fixture.get_by_label("close").click()

    def test_withdrawal_to_merchant(self, setup_fixture):
        """
        同一账号商户转商户(内部)
        """
        time.sleep(3)
        setup_fixture.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
        setup_fixture.get_by_role("button", name="Balance").click()
        setup_fixture.get_by_role("row", name="logo TETH").get_by_role("button").nth(1).click()
        setup_fixture.get_by_label("Enter Address").click()
        setup_fixture.get_by_label("Enter Address").fill("0x390744104E2dbe47B48D336Fa8EaA937df435962")
        setup_fixture.get_by_label("Amount").click()
        setup_fixture.get_by_label("Amount").fill("0.002")
        setup_fixture.get_by_role("button", name="Send").click()
        setup_fixture.get_by_label("Payment Password").click()
        setup_fixture.get_by_label("Payment Password").fill("111111")
        setup_fixture.get_by_label("Email Verification Code").click()
        setup_fixture.get_by_label("Email Verification Code").fill("123456")
        setup_fixture.get_by_role("button", name="Confirm").click()
        time.sleep(5)
        expect(setup_fixture.get_by_text("Transaction successful !")).to_contain_text('Transaction successful !')
        setup_fixture.get_by_label("close").click()

    def test_withdrawal_to_cwalletID(self, setup_fixture):
        """
        通过cwallet ID 转账(内部)
        """
        time.sleep(3)
        setup_fixture.goto("https://admin-test-v2.ccpayment.com/dashboard/index")
        setup_fixture.get_by_role("button", name="Balance").click()
        setup_fixture.get_by_role("row", name="logo DOGE").get_by_role("button").nth(1).click()
        setup_fixture.get_by_label("To Cwallet ID").check()
        setup_fixture.get_by_role("textbox", name="To Cwallet ID").click()
        setup_fixture.get_by_role("textbox", name="To Cwallet ID").fill("9558861")
        setup_fixture.get_by_label("Amount").click()
        setup_fixture.get_by_label("Amount").fill("0.002")
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
        setup_fixture.get_by_label("Payment Password").click()
        setup_fixture.get_by_label("Payment Password").fill("111111")
        setup_fixture.get_by_label("Email Verification Code").click()
        setup_fixture.get_by_label("Email Verification Code").fill("123456")
        setup_fixture.get_by_role("button", name="Confirm").click()
        time.sleep(5)
        expect(setup_fixture.get_by_text("Transaction successful !")).to_contain_text('Transaction successful !')
        setup_fixture.get_by_label("close").click()
