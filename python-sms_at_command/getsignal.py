#!/usr/bin/env python

#get signal
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

def get_signal(device):
    cmd = 'AT+CSQ\r'
    r = command(device, cmd)
    if r[-1] == 'OK' and r[0] == cmd:
        try:
            ret =  r[1].split(':')[1].split(',')[0].strip()
        except:
            ret = -1
        return int(ret)
    else:
        return -2

if __name__ == '__main__':
    try:
        dev = serial.Serial(port='/dev/ttyUSB0')
    except Exception, e:
        print e
        sys.exit(1)
    #
    print 'SIGNAL: %d' %(get_signal(dev))
    #
    dev.close()

