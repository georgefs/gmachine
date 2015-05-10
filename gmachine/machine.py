__all__ = [
        'create',
        'info',
        'kill',
        'rm',
        'start',
        'stop',
        'fab',
        'upload',
        'download',
        'list',
        'fab',
        'get',
        'put',
        'docker_client',
    ]


from gmachine.conf import settings
from gmachine.core import docker_machine
from fabric.api import local, env, run, cd, get, put, sudo
from cache import cache
import docker
import re
import os
import urlparse
import json
from cStringIO import StringIO
import csv
import drivers

def create(machine_name, opts=None):
    if not opts:
        opts = drivers.get_driver_options()
    code = docker_machine.create(machine_name, opts)
    if code:
        raise Exception('error')
    else:
        return machine_name



@cache.cache('gmachine_info')
def info(machine_name):
    result = docker_machine.env(machine_name)
    info = dict(re.findall("([^\s]+)=([^\s]+)", result))
    info['MACHINE_SSH_KEYGEN'] = os.path.join(info['DOCKER_CERT_PATH'], 'id_rsa')
    info['MACHINE_HOST'] = urlparse.urlparse(info['DOCKER_HOST']).hostname

    result = docker_machine.inspect(machine_name)
    data = json.loads(result)

    info['MACHINE_SSH_USER'] = data['Driver']['UserName']
    info['MACHINE_NAME'] = machine_name
    return info


def kill(machine_name):
    docker_machine.kill(machine_name.name)

def rm(machine_name):
    docker_machine.rm(machine_name.name)

def start(machine_name):
    docker_machine.start(machine_name.name)

def stop(machine_name):
    docker_machine.stop(machine_name.name)

def list():
    
    result = docker_machine.list()
    

def fab(machine_name, callback, machine_info=None):
    from cStringIO import StringIO
    machine_info = machine_info or info(machine_name)
    env.user = machine_info['MACHINE_SSH_USER']
    env.key_filename = machine_info['MACHINE_SSH_KEYGEN']
    env.hosts = [ machine_info['MACHINE_HOST'] ]
    env.host_string = env.hosts[0]

    return callback()

def shell(machine_name, cmd, machine_info=None):

    def callback():
        return sudo(cmd)
    return fab(machine_name, callback, machine_info)


def get(machine_name, file_path, machine_info=None):
    from fabric.api import get
    def download():
        path = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        cd(path)
        fp = StringIO()
        get(file_name, fp)
        fp.seek(0)
        return fp

    data =  fab(machine_name, download, machine_info)
    return data

def put(machine_name, files, upload_to, machine_info=None):
    from fabric.api import put

    def upload():
        cd(upload_to)
        put(*files)
        return [os.path.join(upload_to, f) for f in files]

    return fab(machine_name, upload, machine_info)


def docker_client(machine_name, machine_info=None):
    machine_info = machine_info or info(machine_name)
    tls_config = docker.tls.TLSConfig(
        client_cert=(
                os.path.join(machine_info['DOCKER_CERT_PATH'],'cert.pem'),
                os.path.join(machine_info['DOCKER_CERT_PATH'],'key.pem')),
                verify=os.path.join(machine_info['DOCKER_CERT_PATH'],'ca.pem'),
        assert_hostname=False
    )
    client = docker.Client(base_url=machine_info['DOCKER_HOST'].replace('tcp://', 'https://'), tls=tls_config)
    return client

