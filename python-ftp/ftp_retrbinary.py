#!/usr/bin/env python

#FTP retrbinary
#(c) Noprianto, 2010

from ftplib import FTP

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login() #anon
    #
    ret = ftp.retrbinary('RETR /pub/README', open('/tmp/README', 'wb').write)
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()
