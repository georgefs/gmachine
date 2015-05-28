#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus import *

class Azure(FieldSet):
    subscription_id = StringField()
    subscription_cert = StringField()
