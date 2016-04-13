#!/usr/bin/env python

#FTP retrlines, using callback
#(c) Noprianto, 2010

from ftplib import FTP

def func1(line):
    print 'DATA: %s' %(line)
    

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login() #anon
    #
    ret = ftp.retrlines('RETR /pub/README', func1)
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()
