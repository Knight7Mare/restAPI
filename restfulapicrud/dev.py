from manage import *

DEBUG = True

LOGGING =  {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{
        'xyz_console':{
            'class': 'logging.StreamHandler'
        }
    },
    'loggers':{
        'land.middleware': {
            'handlers': ['xyz_console'],
            'level': 'INFO'
        }
    }
}