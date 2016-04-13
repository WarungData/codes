#!/usr/bin/env python

#get all SMS 
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

def get_sms(device, index):
    command(device, 'AT+CMGF=1\r')
    time.sleep(0.2)
    return command(device, 'AT+CMGR=%s\r' %(index))

if __name__ == '__main__':
    try:
        idx = sys.argv[1]
    except:
        print 'usage: %s <index>' %(sys.argv[0])
        sys.exit(1)
    #
    try:
        dev = serial.Serial(port='/dev/ttyUSB0')
    except Exception, e:
        print e
        sys.exit(2)
    #
    print 'Message: ',
    print get_sms(dev, idx)
    #
    dev.close()

