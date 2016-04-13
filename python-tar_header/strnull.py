#!/usr/bin/env python

str = 'test'
strlen = len(str)
maxlen = 100

str += '\x00' * (maxlen-strlen)

print 'str: %s' %(str)
print 'len(str): %d' %(len(str))
