from __future__ import absolute_import

import logging
import sys


class InfoFilter(logging.Filter):
    """for separation of logs in stderr and stout"""

    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)


class Logger:
    @staticmethod
    def get_logger(name) -> logging.Logger:
        """
        Use logging.getLogger as a perfered way to log.
        The said logger provides the functionality to track each request flow using the request id.
        """

        log_format = (
            '%(asctime)s - '
            '%(levelname)s -  '
            '%(name)s - '
            '%(funcName)s - '
            '%(message)s'
        )

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        formatter = logging.Formatter(log_format)

        ''' Log Handlers '''
        ''' stdout handler'''
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.addFilter(InfoFilter())
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)

        ''' stderr handler'''
        stderr_handler = logging.StreamHandler()
        stderr_handler.setLevel(logging.WARNING)
        stderr_handler.setFormatter(formatter)
        logger.addHandler(stderr_handler)

        return logger
