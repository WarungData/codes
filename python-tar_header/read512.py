#!/usr/bin/env python

#read first 512 byte of tarball
#noprianto, GPL.

import sys

f = open(sys.argv[1], 'rb')
header = f.read(512)
f.close()

filename = header[0:100]
filemode = header[100:108] 
ownerid = header[108:116]
groupid = header[116:124]
filesize = header[124:136]
mtime = header[136:148]
checksum = header[148:156]
linkindicator = header[156]
nameoflinkedfile = header[157:257]
ustarmagic = header[257:263]
ustarversion = header[263:265]
ownername = header[265:297]
groupname = header[297:329]
devmajor = header[329:337]
devminor = header[337:345]
prefix = header[345:500]

headerinfo = (filename, filemode, ownerid, groupid,
            filesize, mtime, checksum, linkindicator, 
            nameoflinkedfile, ustarmagic, ustarversion,
            ownername, groupname, devmajor, devminor,
            prefix)

print headerinfo

