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


def scp(from_path, to_path):
    pass

def info(machine_name):
    value = machine.info(machine_name)
    return json.dumps(value, indent=4, sort_keys=True)


def main():
    import clime
    from gmachine import cmd
    clime.start(obj=cmd, black_list=["main", "local"])
