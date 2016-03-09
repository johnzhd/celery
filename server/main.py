from __future__ import absolute_import
from celery import Celery
from config import const


tasks = []
tasks.append('task.task_api')

app = Celery(const.CELERY_MAIN_NAME, include=tasks)
app.config_from_object('config.config')


if __name__ == '__main__':
    app.start()


