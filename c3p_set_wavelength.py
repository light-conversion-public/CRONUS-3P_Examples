#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c3pcontrol - CRONUS-3P remote control Python API.

--- REMOTE CONTROL WARNING ---
This script controls laser devices on the local network and may result in
inadvertent remote control including opening one or more laser shutters. This
can occur if the three conditions are met:
    1) the device IP address is set incorrectly
    2) the remote device SN happens to be correct, e.g. it is default
    3) the remote device has enabled remote control from this host, e.g. the
        remote connection has been used previously
Running the script with a localhost IP address (127.0.0.1) should be safe.

This example shows how to set the wavelength of the tunable output of a
CRONUS-3P laser system.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus3p import C3PControl

target_wavl = 1300
c3p = C3PControl(dev_sn='C3PV2-Virtual', ip_address='127.0.0.1')

curr_wavl = c3p.get_wavelength()
print("Current wavelength is: {} nm".format(curr_wavl))

print("Setting wavelength to {} nm".format(target_wavl))
c3p.set_wavelength(target_wavl)

input("Press any key to close this window")
