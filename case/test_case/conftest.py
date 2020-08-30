import pytest
from selenium import webdriver
from config import globalparam
import time


@pytest.fixture()
def driver_init():
    driver = webdriver.Chrome()
    driver.set_script_timeout(15)
    driver.set_page_load_timeout(15)
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get("https://i2sit.jusdaglobal.com/#/login")
    return driver
    # yield
    # driver.quit()


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    # print(terminalreporter.stats)
    result = dict()
    result["total:"] = str(terminalreporter._numcollected)
    result["passed:"] = str(len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown']))
    result["failed:"] = str(len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown']))
    result["error:"] = str(len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown']))
    result["skipped:"] = str(len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown']))
    result["成功率:"] = str('%.2f' % (len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100)+'%')
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    result["total times:"] = str(duration) + ' seconds'

    with open(globalparam.TEST_RESULT_PATH, 'w', encoding='utf-8') as f:
        for key, value in result.items():
            print(key, value)
            f.writelines(key + value)
            f.write('\n')


# from _pytest import runner
# '''
# # 对应源码
# def pytest_runtest_makereport(item, call):
#     """ return a :py:class:`_pytest.runner.TestReport` object
#     for the given :py:class:`pytest.Item` and
#     :py:class:`_pytest.runner.CallInfo`.
#     """
# '''
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print('------------------------------------')
#
#     # 获取钩子方法的调用结果
#     out = yield
#     # print('用例执行结果', out)
#
#     # 3. 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#     if report.when == "call":
#         print('测试报告：%s' % report)
#         print('步骤：%s' % report.when)
#         print('nodeid：%s' % report.nodeid)
#         print('description:%s' % str(item.function.__doc__))
#         print(('运行结果: %s' % report.outcome))
#
# @pytest.fixture(scope="session", autouse=True)
# def fix_a():
#     print("setup 前置操作")
#     yield
#     print("teardown 后置操作")
