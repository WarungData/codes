#!/usr/bin/env python

#(c) Noprianto, 2010
#GPL

import sys
import zipfile
import glob

def zip_create(zipf, pattern):
    #empty?
    if not pattern:
        print 'Refused to create empty archive'
        return 2
    #open
    try:
        zf = zipfile.ZipFile(zipf, 'w', allowZip64=True)
    except Exception, e:
        print e
        return 3
    #
    errors = []
    for p in pattern:
        files = glob.glob(p)
        for f in files:
            print 'Adding %s' %(f),
            try:
                zf.write(f)
                print 'OK'
            except:
                print 'ERROR'
                errors.append(f)
    #
    zf.close()
    #
    if errors:
        print 'Found %d error(s): ' %(len(errors)),
        print ', '.join(errors)
        return 4
    else:
        print 'OK'
        return 0
    

if __name__ == '__main__':
    try:
        zipf = sys.argv[1]
        pattern = sys.argv[2:]
    except IndexError:
        print 'Usage: %s <zipfile> <pattern> [pattern2...patternN]' %(
            sys.argv[0])
        sys.exit(1)
    #
    sys.exit(zip_create(zipf, pattern))
                
                
