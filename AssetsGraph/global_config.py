# -*- coding: utf-8 -*-

import logging
import os

DEBUG = os.getenv("DEBUG", True)

IP_ADDRESS = os.getenv("IP_ADDRESS", "0.0.0.0")
PORT = os.getenv("PORT", 5000)
PROTOCOL = os.getenv("PROTOCOL", "http://")

VERSION = os.getenv("VERSION", "0.1")
SECRET_KEY = os.getenv(
    "SECRET_KEY", "883de00834f5c0a64d51106751b7606d9782a7af")
DB_URL = os.getenv("DB_URL", "bolt://neo4j:638095@localhost:7687")

X_AUTH_TOKEN = "X-AUTH-TOKEN"
CONTENT_TYPE = "CONTENT-TYPE"
ACCEPT = "ACCEPT"

LOG_ENABLED = False
LOG_LOCATION = os.getenv("LOG_LOCATION", ".")
LOG_FILENAME = os.getenv("LOG_FILENAME", "grest.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", logging.INFO)
LOG_MAX_BYTES = os.getenv("LOG_MAX_BYTES", 1000000)  # 1 Megabyte
LOG_BACKUP_COUNT = os.getenv("LOG_BACKUP_COUNT", 100)
LOG_FORMAT = os.getenv(
    "LOG_FORMAT", "%(levelname)s::%(asctime)-15s::%(process)d::%(filename)s::%(message)s")

QUERY_LIMIT = 20

ENABLE_DELETE_ALL = os.getenv("ENABLE_DELETE_ALL", False)
