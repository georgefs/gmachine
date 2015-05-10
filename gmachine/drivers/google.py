#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus import *


ZONES = {
        "a1": "asia-east1-a",
        "a2": "asia-east1-b",
        "a3": "asia-east1-c",
        
        "e1": "europe-west1-b",
        "e2": "europe-west1-c",
        "e3": "europe-west1-d",

        "u1": "us-central1-a",
        "u2": "us-central1-b",
        "u3": "us-central1-c",
        "u4": "us-central1-f",
    }

MACHINE_TYPES = {
        "s1": "n1-standard-1",
        "s2": "n1-standard-2",
        "s3": "n1-standard-4",
        "s4": "n1-standard-8",
        "s5": "n1-standard-16",
        "s6": "n1-standard-32",

        "m1": "n1-highmem-2",
        "m2": "n1-highmem-4",
        "m3": "n1-highmem-8",
        "m4": "n1-highmem-16",
        "m5": "n1-highmem-32",

        "c1": "n1-highcpu-2",
        "c2": "n1-highcpu-4",
        "c3": "n1-highcpu-8",
        "c4": "n1-highcpu-16",
        "c5": "n1-highcpu-32",

        "f1": "f1-micro",
        "g1": "g1-small",
    }

class Google(FieldSet):
    disk_size = IntField(min_number=10)
    project = StringField()
    machine_type = ChoiceField(choice=MACHINE_TYPES)
    zone = ChoiceField(choice=ZONES)
    scopes = StringField(default="https://www.googleapis.com/auth/devstorage.full_control,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/logging.write")

