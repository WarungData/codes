#!/usr/bin/env python

#send SMS using GSM Modem
#(c) Noprianto, 2010

import sys
import time
import serial

def command(device, cmd):
    device.flush()
    device.write(cmd)
    time.sleep(0.2)
    wait = device.inWaiting()
    read = device.read(wait)
    result = read.strip().split('\r\n')
    return result

def send_sms(device, number, text):
    command(device, 'AT+CMGF=1\r')
    time.sleep(0.2)
    #
    command(device, 'AT+CMGS="%s"\r' %(number))
    time.sleep(0.2)
    #
    command(device, '%s\n' %(text))
    time.sleep(0.2)
    #
    command(device, chr(26))
    #

if __name__ == '__main__':
    try:
        number = sys.argv[1]
        text = sys.argv[2]
    except:
        print 'usage: %s <number> <text>' %(sys.argv[0])
        sys.exit(1)
    #
    try:
        dev = serial.Serial(port='/dev/ttyUSB0')
    except Exception, e:
        print e
        sys.exit(2)
    #
    send_sms(dev, number, text) 
    #
    dev.close()

