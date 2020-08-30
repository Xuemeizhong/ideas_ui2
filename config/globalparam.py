import os


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(BASE_PATH)
DATA_PATH = PROJECT_PATH + r'\data'
ALLURE_REPORT_PATH = PROJECT_PATH + r'\report\allure_report'
XML_REPORT_PATH = ALLURE_REPORT_PATH + r'\xml'
HTML_REPORT_PATH = ALLURE_REPORT_PATH + r'\html'
ALLURE_HTML_PATH = os.path.join(HTML_REPORT_PATH, 'index.html')
LOG_REPORT_PATH = PROJECT_PATH + r'\report\log_report'
FAILURE_IMAGE_PATH = PROJECT_PATH + r'\report\failure_image'

RECEIVE_ADDRESS = ["1363112321@qq.com"]
SEND_ADDRESS_NAME = "zxm2013620@163.com"
SEND_ADDRESS_PWD = "1121zxm2013620"
TEST_RESULT_PATH = PROJECT_PATH + r'\report\test_result\result.txt'

BROWSER_NAME = "MicrosoftEdge"
BROWSER_PATH = r'C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftEdge.exe'


if __name__ == "__main__":
    print(DATA_PATH)
