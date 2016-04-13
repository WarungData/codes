#!/usr/bin/env python

#(c) Noprianto, 2010
#GPL

import sys
import zipfile

def show_zip_info(zipf):
    if not zipfile.is_zipfile(zipf):
        print 'Possibly invalid zip archive: %s' %(zipf)
        return 2
    #
    try:
        zf = zipfile.ZipFile(zipf, 'r', allowZip64=True)
    except Exception, e:
        print e
        return 3
    #
    zl = zf.namelist()
    zf.close()
    #
    for f in zl:
        zi = zf.getinfo(f)
        print '%s: compressed=%d, uncompressed=%d, CRC=%d' %(
            zi.filename,
            zi.file_size,
            zi.compress_size,
            zi.CRC,
            )
    #
    return 0
    

if __name__ == '__main__':
    try:
        zipf = sys.argv[1]
    except IndexError:
        print 'Usage: %s <zipfile>' %(sys.argv[0])
        sys.exit(1)
    #
    sys.exit(show_zip_info(zipf))
                
                
