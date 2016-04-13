#!/usr/bin/env python

#FTP delete
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
    ret = ftp.delete('/ls-nop')
    print ret
    #
    ftp.quit()
    

if __name__ == '__main__':
    main()


#$ python ftp_delete.py 
#USER: nop
#PASSWORD: 
#250 Deleted /ls-nop


#$ python ftp_delete.py 
#USER: nop
#PASSWORD: 
#Traceback (most recent call last):
#  File "ftp_delete.py", line 23, in <module>
#    main()
#  File "ftp_delete.py", line 16, in main
#    ret = ftp.delete('/ls-nop')
#  File "/usr/lib/python2.5/ftplib.py", line 486, in delete
#    resp = self.sendcmd('DELE ' + filename)
#  File "/usr/lib/python2.5/ftplib.py", line 241, in sendcmd
#    return self.getresp()
#  File "/usr/lib/python2.5/ftplib.py", line 216, in getresp
#    raise error_perm, resp
#ftplib.error_perm: 550 Could not delete /ls-nop: No such file or directory
