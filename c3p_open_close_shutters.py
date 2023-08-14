#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c3pcontrol - CRONUS-3P remote control Python API.

--- LASER HAZARD WARNING ---
This script will open one or more laser shutters. Make sure that the beam
leaving the output aperture is properly terminated and that laser safety
precautions are in place.

--- REMOTE CONTROL WARNING ---
This script controls laser devices on the local network and may result in
inadvertent remote control including opening one or more laser shutters. This
can occur if the three conditions are met:
    1) the device IP address is set incorrectly
    2) the remote device SN happens to be correct, e.g. it is default
    3) the remote device has enabled remote control from this host, e.g. the
        remote connection has been used previously
Running the script with a localhost IP address (127.0.0.1) should be safe.

This example shows how to open and close the shutters on a CRONUS-3P laser
system. The program will the user to press ENTER to open and then close the
tunable output shutter.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus3p import C3PControl

c3p = C3PControl(dev_sn='C3PV2-Virtual', ip_address='127.0.0.1')

input("Press ENTER to OPEN all shutters...")
c3p.open_all_shutters()

input("Press ENTER to CLOSE all shutters...")
c3p.close_all_shutters()

input("Press ENTER to close this window")
