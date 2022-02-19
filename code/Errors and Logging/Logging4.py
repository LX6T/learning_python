import logging
import traceback
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')

logger.debug('this is a debug message')

print('\n')
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

print('\n')
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error('The error is: \n%s', traceback.format_exc())
