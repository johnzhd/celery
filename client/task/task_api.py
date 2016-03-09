from __future__ import absolute_import
from celery import Celery
from config import const
app = Celery(const.CELERY_MAIN_NAME)
app.config_from_object('config.config')

@app.task(retry_kwargs={'max_retries': 5})
def run_check(line, name):
    pass

@app.task(retry_kwargs={'max_retries': 5})
def reload_plugins(filter = None, filtertype = None):
    pass

@app.task(retry_kwargs={'max_retries': 5})
def show_plugins_name(filter=None, filtertype = None):
    pass

