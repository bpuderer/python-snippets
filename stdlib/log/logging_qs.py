import logging
import logging.config


def test():
    log.warning('log msg from test func')


logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

log.debug('message at debug level')
log.info('message at info level')
log.warning('message at warning level')
log.error('message at error level')
log.critical('message at critical level')

test()
