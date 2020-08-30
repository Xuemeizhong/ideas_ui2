import pytest
from common import utils
from config import globalparam
from case.page import t01_login_page
import time
from common.log import Log


logger = Log()


test_data = utils.get_test_data(globalparam.DATA_PATH, "login.yaml", "login")


@pytest.mark.parametrize("data", test_data)
def test_login(data, driver_init):
    driver = driver_init
    try:
        t01_login_page.type_name(driver, data["name"])
        t01_login_page.type_pwd(driver, data["pwd"])
        t01_login_page.click_login(driver)

        if "用户名正确、密码正确" in data["title"]:
            actual_name = t01_login_page.get_actul_name(driver)
            assert data["name"] == actual_name
        elif "用户名正确、密码错误" in data["title"]:
            time.sleep(2)
            tip = t01_login_page.get_login_fail_tip(driver)
            assert data["assert"]["tip"] == tip
    except Exception as e:
        logger.error(f'出现异常了，信息如下：\n {e}')
        utils.get_screenshot(driver, globalparam.FAILURE_IMAGE_PATH, data["title"])
        raise
    driver.quit()


if __name__ == "__main__":
    pytest.main(["-s", "-q", r"C:\workspace\iDEAS_sit\case\test_case\test_01_login.py"])
