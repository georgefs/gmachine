#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus import *

CH = ['true', 'false']

REGION = [
    "nyc1",
    "nyc2",
    "nyc3",
    "ams1",
    "ams2",
    "ams3",
    "sfo1",
    "sgp1",
    "lon1"
    ]

class Digitalocean(FieldSet):
    access_token = StringField()
    image = StringField(description="The name of the Digital Ocean image to use, default is docker", default="docker")
    region = ChoiceField(choice=REGION, default="nyc3")
    size = StringField(description="The size of the droplet, format: 512mb", default="512mb")
    ipv6 = ChoiceField(description="Enable IPv6 support for the droplet", default="false", choice=CH)
    private_networking = ChoiceField(description="Enable private networking support for the droplet", default="false", choice=CH)
    backups = ChoiceField(description="Enable backup support for the droplet", default="false", choice=CH)


