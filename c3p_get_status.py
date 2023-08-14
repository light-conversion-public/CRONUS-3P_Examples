#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c3pcontrol - CRONUS-3P remote control Python API.

This example shows how to get the status of a CRONUS-3P laser system.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus3p import C3PControl
import pprint

c3p = C3PControl(dev_sn='C3PV2-Virtual', ip_address='127.0.0.1')

print("\nCRONUS-3P Info:")
pprint.pprint(c3p.get_info())

print("\nCRONUS-3P Status:")
pprint.pprint(c3p.get_status())

print("\nCRONUS-3P Pump laser status:")
pprint.pprint(c3p.get_pump_laser_status())

input("Press ENTER to close this window")
