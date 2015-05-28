#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus import *

class Softlayer(FieldSet):
    api_endpoint = StringField()
    user = StringField()
    api_key = StringField()
    cpu = IntField(descriptions="number of CPUs")
    disk_size = IntField(description="size of the disk in MB", default=0)
    domain = StringField()
    hostname = StringField()
    hourly_billing = BoolField(description="hourly billing instead of monthly billing")
    image = StringField()
    local_disk = BoolField(description=" Use local machine disk instead of softlayer SAN")
    memory = IntField(description="Memory for host in MB")
    private_net_only = BoolField()
    region = StringField()



