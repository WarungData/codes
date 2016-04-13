#!/usr/bin/env python

#FTP retrlines to stdout
#(c) Noprianto, 2010

from ftplib import FTP

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login() #anon
    #
    ret = ftp.retrlines('RETR /pub/README')
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()
