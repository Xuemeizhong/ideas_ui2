import logging
import os
from time import time
from config import globalparam


class Log:
    def __init__(self):
        self.logname = os.path.join(globalparam.LOG_REPORT_PATH, f'{str(time())}.log')

    def __print_console(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if "info" == level:
            logger.info(message)
        elif "debug" == level:
            logger.debug(message)
        elif "warning" == level:
            logger.warning(message)
        elif "error" == level:
            logger.error(message)
        # 把logger的handle移除
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def info(self, message):
        self.__print_console("info", message)

    def debug(self, message):
        self.__print_console("debug", message)

    def warning(self, message):
        self.__print_console("warning", message)

    def error(self, message):
        self.__print_console("error", message)


if __name__ == "__main__":
    logger = Log()
    logger.info("控制台输出info信息")
    logger.debug("控制台输出debug信息")
    logger.warning("控制台输出warning信息")
    logger.error("控制台输出error信息")
