#!/usr/bin/env python

#FTP mkd, rmd
#(c) Noprianto, 2010

from ftplib import FTP
import getpass

def main():
    user = raw_input('USER: ')
    passwd = getpass.getpass('PASSWORD: ')
    #
    ftp = FTP('192.168.0.5')
    ftp.login(user, passwd) 
    #
    ret = ftp.mkd('/nop-test')
    print ret
    #
    ret = ftp.rmd('/nop-test')
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()


#$ python ftp_mkd_rmd.py 
#USER: nop
#PASSWORD: 
#/nop-test
#250 The directory was successfully removed
