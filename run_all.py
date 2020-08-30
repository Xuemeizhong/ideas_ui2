import os
from config import globalparam
from common import utils
from common.send_mail import SendMail


send_mail = SendMail()


if __name__ == "__main__":
    os.system(f'pytest -s -q --alluredir={globalparam.XML_REPORT_PATH}')
    os.system(f'allure generate -c {globalparam.XML_REPORT_PATH} -o {globalparam.HTML_REPORT_PATH}')
    # os.system(f'allure serve {globalparam.HTML_REPORT_PATH}')
    # os.system('allure serve target/allure-results')
    # utils.open_html_file(globalparam.BROWSER_NAME, globalparam.BROWSER_PATH, globalparam.ALLURE_HTML_PATH)
    send_mail.send()
