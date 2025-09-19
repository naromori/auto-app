import logging
import time
from .logger import AppLogger
from typing import Callable
import functools

def autolog(
    on_execution: bool = True,
    on_completion: bool = True,
    log_args: bool = False,
    log_return: bool = False,
    log_timing: bool = False,
    log_level: int = logging.DEBUG,
    logger_name: str = None
):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = AppLogger()
            class_name = ""
            if args and hasattr(args[0], '__class__'):
                class_name = f"{args[0].__class__.__name__}."

            func_name = f"{class_name}{func.__name__}"

            if on_execution:
                msg = f"Executing {func_name}"
                if log_args:
                    msg += f" with args={args}, kwargs={kwargs}"
                logger.log(log_level, msg, "Autolog")

            start_time = time.time() if log_timing else None

            try:
                result = func(*args, **kwargs)

                if on_completion:
                    msg = f"Completed {func_name}"
                    if log_timing:
                        duration = time.time() - start_time
                        msg += f" in {duration:.3f}s"
                    if log_return:
                        msg += f" -> {result}"
                    logger.log(log_level, msg, "Autolog")

                return result

            except Exception as e:
                logger.error(f"Error in {func_name}: {e}", "Autolog")
                raise

        return wrapper
    return decorator