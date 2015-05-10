#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
#__all__ = [
#        'info',
#        'kill',
#        'rm',
#        'start',
#        'stop',
#        'docker',
#        'ssh',
#        'env',
#        'inspect',
#        'ls',
#    ]

from gmachine import machine
from gmachine.core import docker_machine
from fabric.api import local
import json

kill = docker_machine.kill
rm = docker_machine.rm
start = docker_machine.start
stop = docker_machine.stop
ssh = docker_machine.ssh
env = docker_machine.env
inspect = docker_machine.inspect
ls = machine.list
create = machine.create
shell = machine.shell

def get(machine_name, file_path, file_to):
    fi = machine.get(machine_name, file_path)
    with open(file_to, "w+") as f:
        f.write(fi.read())

def put(machine_name, file_path, file_to):
    return machine.put(machine_name, [file_path], file_to)


def info(machine_name):
    value = machine.info(machine_name)
    return json.dumps(value, indent=4, sort_keys=True)

def fab(machine_name, *fabric_args):
    machine_info = machine.info(machine_name)    
    return local("fab -i {} -H {}@{} {}".format(machine_info['MACHINE_SSH_KEYGEN'], machine_info['MACHINE_SSH_USER'], machine_info['MACHINE_HOST'], " ".join(fabric_args)), capture=True)



def main():
    import clime
    from gmachine import cmd
    clime.start(obj=cmd, black_list=["main", "local"])
