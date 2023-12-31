import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
    stream=sys.stdout)