
CELERY_MAIN_NAME  ='celery_test'

TASK_TEMPLATE = '''from __future__ import absolute_import
from celery import Celery
from config import const
app = Celery(const.CELERY_MAIN_NAME)
app.config_from_object('config.config')

'''

USAGE = '''
python celery_test_divide.py [option]

option:
-h        : This usage
-c        : Test client
-s        : Test server
-renew_c  : Create client folder with server codes
'''


