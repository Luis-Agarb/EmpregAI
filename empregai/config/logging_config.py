"""
Centralized logging configuration for EmpregAI.
"""

import logging

from empregai.config.settings import settings


def setup_logger(name: str = "EmpregAI") -> logging.Logger:
    """
    Create and configure a logger.

    Args:
        name: Logger name.

    Returns:
        logging.Logger: Configured logger instance.
    """

    logs = logging.getLogger(name)

    if logs.handlers:
        return logs

    logs.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logs.addHandler(console_handler)
    logs.propagate = False

    return logs


logs = setup_logger()