import logging
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
# handler1 = RotatingFileHandler('app.log', maxBytes=2000, backupCount=3)
# logger.addHandler(handler1)

# for _ in range(1000):
#     logger.info('Hello, world!')


# s, m, h, d, midnight, w0
handler2 = TimedRotatingFileHandler('timed_test.log', when='s', interval=2, backupCount=3)
logger.addHandler(handler2)

for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(1)

