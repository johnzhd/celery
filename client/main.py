import sys
import os

from task import task_api

from celery import group
from celery import chord
from celery import chain
from celery import chunks
 

os.chdir(os.path.split(os.path.realpath(__file__))[0])
import time


def start():
    print(__name__)
    ch = group(task_api.run_check.s('{"json":"json"}', name) for name in task_api.show_plugins_name.apply_async().get())
    ret = ch()
    print(ret.get())

start()


