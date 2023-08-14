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

This example shows how to control the tunable output of a CRONUS-3P laser
system. The program will set the wavelength and GDD, the user will then need to
press ENTER to open and then close the output shutter.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""
from lightcon.cronus3p import C3PControl

target_wavl = 1300
target_gdd = -2500
c3p = C3PControl(dev_sn='C3PV2-Virtual', ip_address='127.0.0.1')

curr_wavl = c3p.get_wavelength()
print("Current wavelength is: {} nm".format(curr_wavl))
curr_gdd = c3p.get_gdd()
print("Current GDD is: {} fs2".format(curr_gdd))

print("Setting wavelength to {} nm".format(target_wavl))
c3p.set_wavelength(target_wavl)
print("Setting GDD to {} fs2".format(target_gdd))
c3p.set_gdd(target_gdd)

input("Press ENTER to OPEN tunable output shutter...")

print("Opening main output shutter")
c3p.open_all_shutters()

print("Press ENTER to CLOSE tunable output shutter...")

print("Closing shutters and setting back to {} nm and {} fs2".format(
    curr_wavl, curr_gdd))
c3p.close_all_shutters()
c3p.set_wavelength(curr_wavl)
c3p.set_wavelength(curr_gdd)

input("Press ENTER to close this window")
