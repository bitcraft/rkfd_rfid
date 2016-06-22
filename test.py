#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Test file for reading rfid key fobs

# list of badge #'s
ok = ["0008103620"]

while 1:
    data = raw_input("scan...")
    if data in ok:
        print("open!")
    else:
        print("no!")
