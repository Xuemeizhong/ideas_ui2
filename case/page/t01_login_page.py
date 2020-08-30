from selenium.webdriver.common.by import By


NAME_INPUT_ELEMENT = (By.XPATH, "//input[@placeholder='请输入用户名']")
PWD_INPUT_ELEMENT = (By.XPATH, "//input[@placeholder='请输入密码']")
LOGIN_BUTTON_ELEMENT = (By.CLASS_NAME, "submit-btn")
LOGIN_FAIL_TIP_ELEMENT = (By.XPATH, "//div[@class='thorn6-message']")
ACTUAL_NAME_TEXT_ELEMENT = (By.XPATH, "//span[@class='el-dropdown-link']")


def type_name(driver, name):
    driver.find_element(*NAME_INPUT_ELEMENT).send_keys(name)


def type_pwd(driver, pwd):
    driver.find_element(*PWD_INPUT_ELEMENT).send_keys(pwd)


def click_login(driver):
    driver.find_element(*LOGIN_BUTTON_ELEMENT).click()


def get_login_fail_tip(driver):
    return driver.find_element(*LOGIN_FAIL_TIP_ELEMENT).text


def get_actul_name(driver):
    return driver.find_element(*ACTUAL_NAME_TEXT_ELEMENT).text
