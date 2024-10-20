import os
import logging


LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter(LOG_FORMAT)

stream_handler.setFormatter(formatter)
stream_handler.setLevel(LOG_LEVEL)

logger.addHandler(stream_handler)