from __future__ import absolute_import
from server.main import app

from task import load_frame



manager = load_frame.plugins_manager()

@app.task(retry_kwargs={'max_retries': 5})
def run_check(line, name):
    ### for test ###
    print(line, name)
    ################
    try:
        task = manager.adapter_json(line)
        if not task:
            return line
        plugin = manager.create_by_name(name)
        if not plugin:
            return line
        if plugin.start(task):
            line = task.dumps()
        return line
    except Exception as e:
        return line


@app.task(retry_kwargs={'max_retries': 5})
def reload_plugins(filter = None, filtertype = None):
    try:
        return manager.reload(filter, filtertype)
    except Exception as e:
        return False

@app.task(retry_kwargs={'max_retries': 5})
def show_plugins_name(filter=None, filtertype = None):
    ### for test ###
    return ['first', 'second', 'third']
    ################
    try:
        return manager.show(filter, filtertype)
    except Exception as e:
        return None





