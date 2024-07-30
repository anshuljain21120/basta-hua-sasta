import logging

from basta_hua_sasta.commons.logger import Logger

default_logger = Logger.get_logger("LoggingDecorator")


def log_fn(logger=default_logger):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            fn_name = f.__name__
            try:
                logger.info(f"Fn {fn_name} called with args: [args: {args}, kwargs: {kwargs}]")
                result = f(*args, **kwargs)
                logger.info(f"Fn {fn_name} executed & returned: {result}")
                return result
            except Exception as e:
                logger.exception(f"Exception raised in {fn_name}. exception: {str(e)}")
                raise e
        return wrapped_f
    return wrap
