#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# for reading rfid key fobs
import sqlite3 as lite
import RPi.GPIO as GPIO
import sys

# Setup GPIO
GPIO.setmode(GPIO.BOARD) 

while 1:
    rawIn = raw_input("Scan...") # We are waiting here for input
    rfidScan = rawIn.strip() # remove CR or NL character(s)
    print("Scanned ID")

    # reconnect to sqlite db every time
    con = lite.connect('rms.db')
    
    with con:    
        cur = con.cursor()
        #cur.execute("CREATE TABLE Members(Id INT, Name TEXT, Status TEXT, Rfid TEXT)")
        #cur.execute("INSERT INTO Members VALUES(1,'Doug Heimbecker','Active','0004269356')")
        #cur.execute("INSERT INTO Members VALUES(2,'Dez Troyer','Banished!','0009963630')")
        cur.execute("SELECT * FROM Members WHERE Rfid = :Rfid", {"Rfid": rfidScan})
        con.commit()
        row = cur.fetchone()           

        if (row != None):
            memberId = row[0]
            memberName = row[1]
            memberStatus = row[2]
            rfidCheck = row[3]
            
        if (row != None and rfidCheck == rfidScan            
                and memberStatus == "Active"):
            print("Great welcome, " + memberName + " (" + str(memberId) + ")")
            print("Hence, go forth, and flourish unto thy Makerdom!")

            # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
            
            
        else:
            print("Fly, you fool! Fly!")
            print("|" + rfidCheck + "|" + rfidScan + "|")
            print("|" + memberStatus + "|" + str(cur.rowcount) + "|")
        


