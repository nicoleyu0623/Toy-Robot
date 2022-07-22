# @Time : 22/7/22 6:18 pm
# @Original Author : Nicole Yu
# @File : log_util.py
# @Project: AUTOMATION
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

"""
    This module create a logging factory for logging purpose

"""


class LogUtils(object):
    VERBOSE_FMT = (
        "%(levelname)s %(asctime)s %(name)s %(module)s %(process)d %(thread)d "
        "%(filename)s_%(lineno)s_%(funcName)s  %(message)s"
    )

    @classmethod
    def get_rotating_file_logger(
        cls, logger_name, filename, max_bytes=100 * 1024 * 1024, backup_count=10
    ):
        """

        :param logger_name:
        :param filename:
        :param max_bytes:
        :param backup_count:
        :return:
        """
        logger = logging.getLogger(logger_name)
        fmtter = logging.Formatter(fmt=cls.VERBOSE_FMT)
        handler = RotatingFileHandler(
            filename,
            mode="w",
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )

        return cls._make_logger(fmtter, handler, logger)

    @classmethod
    def get_stream_logger(cls, logger_name="CONSOLE_DEBUGGER"):
        """generate a standard output logger, used for debugging

        :param logger_name:
        :return:
        """
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter(fmt=cls.VERBOSE_FMT)
        handler = StreamHandler()
        return cls._make_logger(formatter, handler, logger)

    @classmethod
    def _make_logger(cls, formatter, handler, logger):
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger


# LOGGER = LogUtils.get_stream_logger()
LOGGER = LogUtils.get_rotating_file_logger(
    logger_name="toy-robot-logger", filename="toy-robot.log"
)
