# 11_10.py
# (c) Noprianto <nop@noprianto.com> GPL
#
# Dump/backup database
# Restore database

import base64
import oerpapi

host = raw_input('Server: ')

print 'Mencoba melakukan koneksi ke %s pada port default...' %(host)
client = oerpapi.OErpClient(host)
client.connect()

version = client.version()
print 'Versi: %s' %(version.get('server_version'))

db = client.get_db()
db_list = db.list()
print 'Database yang tersedia: %s' %(db_list)

db_name = raw_input('Database yang ingin dibackup: ')

admin_password = raw_input('Masukkan password admin: ')
db.admin_password = admin_password

fout = '/tmp/backup.sql'

print 'Mohon tunggu...'
backup = db.dump(db_name)
if backup:
    f = open('/tmp/backup.sql', 'wb')
    f.write(base64.decodestring(backup))
    f.close()
    print 'Backup disimpan pada %s' %(fout)
else:
    print 'Backup gagal didapatkan'
    
db_name = raw_input('Ingin restore %s ke database: ' %(fout))
db.restore(db_name, backup)

