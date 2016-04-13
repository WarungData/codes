#!/usr/bin/env python

#FTP connect, LIST
#(c) Noprianto, 2010

from ftplib import FTP

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login() #anon
    ret = ftp.retrlines('LIST')
    ftp.quit()
    #
    print ret
    

if __name__ == '__main__':
    main()
