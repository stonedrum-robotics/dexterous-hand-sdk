"""Logging utilities."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger for SDK and ROS-adjacent code.

    The helper intentionally uses the standard library only so it behaves the
    same in standalone Python examples, pytest, and ROS 2 launch contexts. It
    installs one stream handler per logger name and leaves existing handlers in
    place when a ROS node or application has already configured logging. The
    logger remains propagating so host applications can still capture records.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s [%(name)s] %(levelname)s %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
