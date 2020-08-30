import yaml
import os
import time
import webbrowser
from common.log import Log


logger = Log()


def get_test_data(data_path, file_name, case_name):
    file_path = os.path.join(data_path, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.Loader).get(case_name)
            return data
    else:
        raise FileNotFoundError(f'未找到文件{file_path}！！！')


def get_screenshot(driver, img_path, case_name):
    now_time = time.strftime("%Y%m%d.%H.%M.%S")
    t = driver.get_screenshot_as_file(os.path.join(img_path, f'{case_name}_{now_time}.jpg'))
    logger.info(f'截图结果：{t}')


def open_html_file(browser_name, browser_path, html_file_path):
    webbrowser.register(browser_name, None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.open_new_tab(html_file_path)
