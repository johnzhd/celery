import sys
import os
import args
import shutil 
from config import const

print(os.path.split(os.path.realpath(__file__))[0])
os.chdir(os.path.split(os.path.realpath(__file__))[0])

cmd = args.args()

print(cmd)

if cmd.get('c'):
    os.system('python client/main.py')
elif cmd.get('s'):
    import socket
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    os.system('celery worker -A server.main -l info -n {0}'.format(myaddr))
elif cmd.get('renew_c'):
    ## delete  folder: client/config
    ## delete  folder: client/task
    ## copy ./config to client/config
    ## new     folder: client/task
    ## new       file: client/task/__init__.py
    ## new       file: client/task/task_api.py
    ## read ./task/task_api.py | filter | client/task/task_api.py
    # client.config
    if os.path.exists('client/config'):
        shutil.rmtree('client/config')
    if os.path.exists('client/task'):
        shutil.rmtree('client/task')
    shutil.copytree('config', 'client/config')
    # client.task
    shutil.rmtree('client/task')
    os.mkdir('client/task')
    f = open('client/task/__init__.py', 'w')
    f.close()
    buff = const.TASK_TEMPLATE
    mark = 0
    for line in open('task/task_api.py', 'r'):
        line = line.strip()
        if len(line) == 0:
            continue
        if mark == 0:
            if line[0] == '@':
                buff += line + '\n'
                mark = 1
        elif mark == 1:
            buff += line + '\n'
            buff += '    pass' + '\n'
            buff += '\n'
            mark = 0
    f = open('client/task/task_api.py', 'w')
    f.write(buff)
    f.close()
else:
    print(const.USAGE)

