from fabric.api import run
from fabric.api import sudo

def deploy(path='/opt/sites/flisol-connect/'):
    run('cd {0} && git pull && source ../bin/activate && pip install -r requirements.txt && ./manage.py migrate && ./manage.py collectstatic --noinput'.format(path))
    sudo("""/etc/init.d/supervisor stop && ps aux | grep wsgi | grep -v grep | gawk '{a="kill -9 "$2;system(a)}'""")
    sudo('/etc/init.d/supervisor start')
