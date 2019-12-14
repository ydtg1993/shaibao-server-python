import os
import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }  # 日志级别关系映射

    format = '{"levelname": "%(levelname)s", "asctime": "%(asctime)s", "location": "%(filename)s:%(lineno)d", "process": "%(process)d", "info": %(message)s}'

    base_url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    base_log_url = os.path.join(base_url, 'log_file')

    def __init__(self, file_name='default', log_name='all.log', level='info', when='D', back_count=3, fmt=format):
        this_log_url = os.path.join(self.base_log_url, file_name)
        os.mkdir(this_log_url) if not os.path.isdir(this_log_url) else ...
        log_url = os.path.join(this_log_url, log_name)
        self.logger = logging.getLogger(log_url)
        format_str = logging.Formatter(fmt)                     # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))   # 设置日志级别
        sh = logging.StreamHandler()                            # 往屏幕上输出
        sh.setFormatter(format_str)                             # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(
            filename=log_url,
            when=when,
            backupCount=back_count,
            encoding='utf-8'
        )  # 往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)                             # 设置文件里写入的格式
        self.logger.addHandler(sh)                              # 把对象加到logger里
        self.logger.addHandler(th)
