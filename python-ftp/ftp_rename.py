#!/usr/bin/env python

#FTP rename
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
    ret = ftp.rename('/ls-nop', '/ls')
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()


#$ python ftp_rename.py 
#USER: nop
#PASSWORD: 
#250 File successfully renamed or moved

