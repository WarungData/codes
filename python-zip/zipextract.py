#!/usr/bin/env python

#(c) Noprianto, 2010
#GPL
#only tested under Linux

import sys
import os
import time
import zipfile
from stat import *

def zip_extract(zipf, destdir):
    #valid?
    if not zipfile.is_zipfile(zipf):
        print 'Possibly invalid zip archive: %s' %(zipf)
        return 2
    #abspath
    destdir = os.path.abspath(destdir)
    #mkdir
    try:
        os.mkdir(destdir)
    except OSError, e:
        #already exists
        pass
    #writable?
    if not os.access(destdir, os.W_OK):
        print 'Unable to write to %s' %(destdir)
        return 4
    #open
    try:
        zf = zipfile.ZipFile(zipf, 'r', allowZip64=True)
    except Exception, e:
        print e
        return 3
    #iterate
    zl = zf.namelist()
    #
    #create directories
    dirs = []
    for f in zl:
        if f.find('/') > -1: #check
            d = f.split('/') #check
            d2 = d[:-1]
            if not d2 in dirs:
                dirs.append(d2)
    for d in dirs:
        prev = ''
        for d2 in d:
            d3 = os.path.join(prev, d2)
            prev = d3
            d4 = os.path.join(destdir, d3)
            try:
                print 'Creating directory %s' %(d4)
                os.mkdir(d4)
            except:
                pass
    #
    for f in zl:
        zi = zf.getinfo(f)
        fname = os.path.join(destdir, zi.filename)
        #dir?
        if not fname.endswith('/'): #not dir, check
            print 'Extracting %s' %(fname)
            #write file
            o = open(fname, 'wb')
            o.write(zf.read(zi.filename))
            o.close()
            #file mtime
            y, m, d, h, i, s = zi.date_time
            ftime = time.mktime((y, m, d, h, i, s, -1, -1, -1))
            try:
                os.utime(fname, (ftime, ftime))
            except Exception, e:
                pass
            #file mode
            mode = zi.external_attr >> 16L
            if not mode:
                mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH
            os.chmod(fname, mode)
            
            
    #close
    zf.close()
    return 0
    

if __name__ == '__main__':
    try:
        zipf = sys.argv[1]
        destdir = sys.argv[2]
    except IndexError:
        print 'Usage: %s <zipfile> <destdir>' %(sys.argv[0])
        sys.exit(1)
    #
    sys.exit(zip_extract(zipf, destdir))
                
                
