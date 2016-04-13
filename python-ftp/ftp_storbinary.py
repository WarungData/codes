#!/usr/bin/env python

#FTP storbinary
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
    ret = ftp.storbinary('STOR /ls-nop', open('/bin/ls', 'rb'))
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()



#$ python ftp_storbinary.py 
#USER: nop
#PASSWORD: 
#226-File successfully transferred
#226 0.051 seconds (measured here), 1.52 Mbytes per second

