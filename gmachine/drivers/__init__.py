#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
import inspect

from raw_input_plus import *
import os
import importlib
def __scan_drivers():
    drivers = {}
    curr_path = os.path.abspath(os.path.dirname(__file__))
    fs = os.listdir(curr_path)
    for f in fs:
        if f == '__init__.py' or not f.endswith('.py'):
            continue
        module_name = f[:-3]
        module = importlib.import_module("gmachine.drivers."+module_name)

        for attr in dir(module):
            obj = getattr(module, attr)
            if obj != FieldSet and inspect.isclass(obj) and issubclass(obj, FieldSet):
                drivers[module_name] = obj()
    return drivers


def get_driver_options():
    create_opts = {}

    drivers = __scan_drivers()
    driver = ChoiceField(choice=drivers.keys()).raw_input()
    driver_opts = drivers[driver].raw_input()
    
    create_opts['--driver'] = driver

    for opt, value in driver_opts.items():
        create_opts["--{}-{}".format(driver, opt.replace('_', '-'))] = value

    opts = ["{} {}".format(opt, value) for opt, value in create_opts.items()]

    return opts

