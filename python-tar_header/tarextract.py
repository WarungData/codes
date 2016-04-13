#!/usr/bin/env python

#tarextract.py
#extract tarball
#from scratch (without using tarfile module)
#(c) Noprianto, 2008, GPL.
#
#v0
#
#todo: 
#- test: charspecial, blockspecial, fifo, hardlink
#- BIG code cleanup, algorithm check
#- general error check
#- checksum
#- linkindicator 7
#
#

import sys
import os


def getvalue(data, type='int', base=8):
    if type == 'string':
        return data.replace('\x00','').strip()
    elif type == 'int':
        temp = data.replace('\x00','').strip()
        if temp:
            return int(temp, base)
        else:
            return 0
    else:
        return None

if len(sys.argv) < 2:
    sys.exit('usage : tarextract.py <tarball>')

f = open(sys.argv[1], 'rb')
while True:
    header = f.read(512)
    filename = getvalue(header[0:100], 'string')
    filemode = getvalue(header[100:108])
    ownerid = getvalue(header[108:116])
    groupid = getvalue(header[116:124])
    filesize = getvalue(header[124:136])
    mtime = getvalue(header[136:148])
    checksum = getvalue(header[148:156])
    linkindicator = header[156]
    nameoflinkedfile = getvalue(header[157:257], 'string')
    ustarmagic = header[257:263]
    ustarversion = header[263:265]
    ownername = getvalue(header[265:297], 'string')
    groupname = getvalue(header[297:329], 'string')
    devmajor = getvalue(header[329:337])
    devminor = getvalue(header[337:345])
    prefix = getvalue(header[345:500], 'string')

    blockcount = (filesize/512) + 1

    if not header or not filename.strip():
        break

    if linkindicator == '0' or linkindicator == '\x00':
        #reg file
        if filename.find('/'):
            dirs = filename.split('/')
            path = ''
            for d in dirs[:-1]:
                path += d + '/'
                if not os.path.exists(path):
                    os.mkdir(path, filemode)

        f2 = open(filename, 'wb')
        for i in range(blockcount):
            left = filesize - (i * 512)
            buf = f.read(512)[:left]
            f2.write(buf)
        f2.close()
        os.chmod(filename, filemode)
    elif linkindicator == '1':
        #hardlink
        if os.path.exists(filename):
            os.unlink(filename)
        os.link(nameoflinkedfile, filename)
    elif linkindicator == '2':
        #symlink
        if os.path.exists(filename):
            os.unlink(filename)
        os.symlink(nameoflinkedfile, filename)
    elif linkindicator == '3':
        #char special
        if os.path.exists(filename):
            os.unlink(filename)
        dev = os.makedev(devmajor, devminor)
        os.mknod(filename, filemode | S_IFCHR, dev)
    elif linkindicator == '4':
        #block special
        if os.path.exists(filename):
            os.unlink(filename)
        dev = os.makedev(devmajor, devminor)
        os.mknod(filename, filemode | S_IFBLK, dev)
    elif linkindicator == '5':
        #dir
        if os.path.exists(filename):
            os.rmdir(filename)
        os.mkdir(filename, filemode)
    elif linkindicator == '6':
        #fifo
        if os.path.exists(filename):
            os.unlink(filename)
        os.mknod(filename, filemode | S_IFIFO)
    elif linkindicator == '7':
        if ustarmagic.strip().lower() == 'ustar':
            pass
            #fixme: nop: reserved on GNU tar?
        else:
            pass
            #fixme: nop: not yet implemented now
    
    os.utime(filename, (-1, mtime))


