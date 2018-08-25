import os
import shlex
import subprocess


os.environ['PYTEST'] = 'PYTEST val'
print('PYTEST environment variable:', os.getenv('PYTEST', 'default val'))


cmd = 'tail -n4 etree_parse.py'
cmd_args = shlex.split(cmd)
print(f'{cmd} : {cmd_args}')


# https://docs.python.org/3/library/subprocess.html?highlight=subprocess#subprocess.run
cp = subprocess.run(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(cp)
