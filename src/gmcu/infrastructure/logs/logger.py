import logging.config

logger = logging.getLogger(__name__)

def setupLogger():
  logging.config.dictConfig({
      'version': 1,
      'disable_existing_loggers': False,
      'formatters': {
          'standard': {
              'format': '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
          },
      },
      'handlers': {
          'console': {
              'class': 'logging.StreamHandler',
              'level': 'INFO',
              'formatter': 'standard',
              'stream': 'ext://sys.stdout',
          },
      },
      'loggers': {
          'root': {
              'handlers': ['console'],
              'level': 'INFO',
              'propagate': True,
          },
      },
  })
