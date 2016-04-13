# 11_5.py
# (c) Noprianto <nop@noprianto.com> GPL
#
# Mendapatkan daftar database
# Memilih database
# Login ke database

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

db_name = raw_input('Database yang ingin digunakan: ')
if not db.exist(db_name):
    print 'Database %s tidak ditemukan' %(db_name)
else:
    user = raw_input('[%s] Masukkan nama user: ' %(db_name))
    password = raw_input('[%s] Masukkan password: ' %(db_name))
    print 'Mencoba login...'
    client.login(db_name, user, password)
    print 'UserID adalah: %s' %(client.uid)

