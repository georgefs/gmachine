#! /usr/bin/env python
from gmachine.conf import settings
import os
from fabric.api import local

class Docker_Machine(object):
    def __init__(self, machine_path, store_path=None):
        self.machine_path = machine_path
        if not store_path:
            store_path = os.path.join(os.environ.get('HOME'), ".docker/machine")
        self.store_path = store_path

    def __execute__(self, cmd, capture=True, direct=False):
        if isinstance(cmd, list):
            cmd = " ".join(cmd)
        elif not isinstance(cmd, basestring):
            raise Exception('type error')

        cmd = '{} --storage-path "{}" {}'.format(self.machine_path, self.store_path, cmd)
        if direct:
            return os.system(cmd)
        else:
            return local(cmd, capture=capture)


    def create(self, machine_name, opts ):
        result = self.__execute__(['create', machine_name ] + opts, direct=True)
        return result

    def env(self, machine_name):
        return self.__execute__(['env', machine_name])

    def inspect(self, machine_name):
        return self.__execute__(['inspect', machine_name])

    def env(self, machine_name):
        return self.__execute__(['env', machine_name])

    def kill(self, machine_name):
        return self.__execute__(['kill', machine_name], direct=True)

    def rm(self, machine_name):
        return self.__execute__(['rm', machine_name], direct=True)

    def ssh(self, machine_name):
        return self.__execute__(['ssh', machine_name], capture=False, direct=True)

    def start(self, machine_name):
        return self.__execute__(['start', machine_name], direct=True)

    def stop(self, machine_name):
        return self.__execute__(['stop', machine_name], direct=True)

    def list(self):
        return self.__execute__(['ls'], direct=True)


docker_machine = Docker_Machine(settings.DOCKER_MACHINE_PATH, settings.DOCKER_MACHINE_STORAGE_PATH)
