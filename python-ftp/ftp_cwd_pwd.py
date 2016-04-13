#!/usr/bin/env python

#FTP connect, cwd, pwd
#(c) Noprianto, 2010

from ftplib import FTP

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login() #anon
    #
    ret = ftp.cwd('/pub')
    print ret
    #
    ret = ftp.pwd()
    print ret
    #
    ret = ftp.retrlines('LIST')
    print ret    
    #
    ftp.quit()
    
    

if __name__ == '__main__':
    main()
