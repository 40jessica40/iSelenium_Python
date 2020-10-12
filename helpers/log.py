# -*- coding: utf-8 -*-
# By: Racheliiiiiiiii9999
import logging
import os
import sys
import time

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')

# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)


class Log:
    def __init__(self):

        # 文件的命名
        self.work_filename = sys.argv[0][sys.argv[0].rfind(os.sep) + 1:][-3:0]
        self.log_name = os.path.join(log_path, '%s' % time.strftime('%Y_%m_%d_%H_%M_%S')+'_'+sys.argv[0][sys.argv[0].rfind(os.sep) + 1:][0:-3]+".log")
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - '+sys.argv[0][sys.argv[0].rfind(os.sep) + 1:][0:-3]+'] - %(levelname)s: %(message)s')

    def __console(self, level, message):

        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

