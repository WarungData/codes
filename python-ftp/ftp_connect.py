#!/usr/bin/env python

#FTP connect
#(c) Noprianto, 2010

from ftplib import FTP

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login() #anon
    welcome = ftp.getwelcome()
    ftp.quit()
    #
    print welcome
    

if __name__ == '__main__':
    main()
