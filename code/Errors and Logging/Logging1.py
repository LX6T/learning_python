import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')            # DEBUG
logging.info('This is a info message')              # INFO
logging.warning('This is a warning message')        # WARNING   (printed by default)
logging.error('This is a error message')            # ERROR     (printed by default)
logging.critical('This is a critical message')      # CRITICAL  (printed by default)

import Logging2