#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus import *

INSTANCE_TYPE = [
       "t2.micro",
       "t2.small",
       "t2.medium",
       "m3.medium",
       "m3.large",
       "m3.xlarge",
       "m3.2xlarge",
       "m1.small",
       "m1.medium",
       "m1.large",
       "m1.xlarge",
       "c4.large",
       "c4.xlarge"
       "c4.2xlarge",
       "c4.4xlarge",
       "c4.8xlarge",
       "c3.large",
       "c3.xlarge",
       "c3.2xlarge",
       "c3.4xlarge",
       "c3.8xlarge",
       "c1.medium",
       "c1.xlarge",
       "cc2.8xlarge",
       "r3.larg",
       "r3.xlarge",
       "r3.2xlarge",
       "r3.4xlarge",
       "r3.8xlarge",
       "m2.xlarge",
       "m2.2xlarge",
       "m2.4xlarge",
       "cr1.8xlarge",
       "i2.xlarge",
       "i2.2xlarge",
       "i2.4xlarge",
       "i2.8xlarge",
       "d2.xlarge",
       "d2.2xlarge",
       "d2.4xlarge",
       "d2.8xlarge",
       "hi1.4xlarge",
       "hs1.8xlarge",
       "t1.micro",
       "g2.2xlarge",
       "g2.8xlarge",
       "cg1.4xlarge"    
    ]

REGION = [
        "us-east-1",
        "us-west-1",
        "us-west-2",
        "ap-northeast-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "eu-central-1",
        "eu-west-1",
        "sa-east-1"
        
        ]

ZONE = ['a', 'b', 'c', 'd', 'e']

class Amazonec2(FieldSet):
    access_key = StringField()
    ami = StringField(description="your ami id", default="ami-4ae27e22")
    #iam_instance_profile = 
    instance_type = ChoiceField(choice=INSTANCE_TYPE, default="m1.small")
    region = ChoiceField(choice=REGION, default="us-east-1")
    root_size = IntField(default=16)
    secret_key = StringField()
    security_group = StringField(default="docker-machine")
    session_token = StringField()
    subnet_id = StringField(description="AWS VPC subnet id")
    vpc_id = StringField()
    zone = ChoiceField(choice=ZONE, default="a")

