#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
import os

user_setting = os.environ.get("GMACHINE_SETTINGS", "")

CONF_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.join(CONF_PATH, "..")

if user_setting:
    user_setting = __import__(user_setting)


get_opt = lambda opt_name, default_opt_value=None: getattr(user_setting, opt_name, None) or os.environ.get(opt_name, default_opt_value)




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
    return os.path.join(ROOT_PATH + "/bin", path)


DOCKER_MACHINE_PATH = get_opt("DOCKER_MACHINE_PATH", get_platform_machine())
assert DOCKER_MACHINE_PATH

DOCKER_MACHINE_STORAGE_PATH = get_opt("DOCKER_MACHINE_STORAGE_PATH", None)


GMACHINE_CACHE_TIME = 60
