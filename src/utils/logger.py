# utils/logger.py

import logging

def setup_logger(name="system_logger", log_level=logging.INFO):
    """Set up a logger to log messages."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger

def log_metrics(logger, metric_name, value):
    """Log system metrics (e.g., performance data, API usage)."""
    logger.info(f"{metric_name}: {value}")
