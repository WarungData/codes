#!/usr/bin/env python

#get GSM modem info
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

def get_manufacturer(device):
    return command(device, 'AT+CGMI\r')

def get_model(device):
    return command(device, 'AT+CGMM\r')

def get_imei(device):
    return command(device, 'AT+CGSN\r')

def get_sw_version(device):
    return command(device, 'AT+CGMR\r')

def get_msisdn(device):
    return command(device, 'AT+CNUM\r')

def get_imsi(device):
    return command(device, 'AT+CIMI\r')

if __name__ == '__main__':
    try:
        dev = serial.Serial(port='/dev/ttyUSB0')
    except Exception, e:
        print e
        sys.exit(1)
    #
    print 'MANUFACTURER: ', 
    print get_manufacturer(dev)
    print 'MODEL: ',
    print get_model(dev)
    print 'IMEI: ',
    print get_imei(dev)
    print 'SOFTWARE: ',
    print get_sw_version(dev)
    print 'MSISDN: ',
    print get_msisdn(dev)
    print 'IMSI: ',
    print get_imsi(dev)
    #
    dev.close()

