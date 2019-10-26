from libs.log.setup import setup_logging

# flake8: noqa: F403
# pylint:disable=wildcard-import, unused-wildcard-import
# noinspection PyUnresolvedReferences
from .base import *

DEBUG = False

setup_logging(DEBUG)

ALLOWED_HOSTS = ['127.0.0.1', ]

# HSTS
SECURE_HSTS_SECONDS = 31536000  # 365 * 24 * 60 * 60
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
