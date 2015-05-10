#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from gmachine.core import settings



DOCKER_MACHINES = {
    "Linux": {
        "64bit": "docker-machine_linux-amd64",
        "32bit": "docker-machine_linux-386",
    },
    "Darwin": {
        "64bit": "docker-machine_darwin-amd64",
        "32bit": "docker-machine_linux-386",
    },
    "Windows": {
        "64bit": "docker-machine_windows-amd64.exe",
        "32bit": "docker-machine_windows-386.exe",
    }
}
def get_platform_machine():
    import platform
    import os
    path = DOCKER_MACHINES[platform.system()][platform.architecture()[0]]
    return os.path.join(ROOT_PATH, path)
