# 11_9.py
# (c) Noprianto <nop@noprianto.com> GPL
#
# Membuat database
# Mengganti nama database
# Mengopi database
# Menghapus database

import oerpapi

host = raw_input('Server: ')

print 'Mencoba melakukan koneksi ke %s pada port default...' %(host)
client = oerpapi.OErpClient(host)
client.connect()

version = client.version()
print 'Versi: %s' %(version.get('server_version'))

db = client.get_db()
admin_password = raw_input('Masukkan password admin: ')
db_name = raw_input('Masukkan nama database yang ingin dibuat: ')
password = raw_input('Masukkan password yang ingin digunakan: ')
demo = False
if raw_input('Input Y apabila ingin menggunakan contoh data: ') == 'Y':
    demo = True

db.admin_password = admin_password
print 'Mohon tunggu...'
db.create(db_name, demo, 'id_ID', password)
print db.list()

new_name = raw_input('Masukkan nama database yang baru (ENTER=lewatkan): ')
new_name = new_name.strip()
if new_name:
    db.rename(db_name, new_name)
    db_name = new_name
print db.list()

copy_name = raw_input('Mengopi database ke (ENTER=lewatkan): ')
copy_name = copy_name.strip()
if copy_name:
    db.duplicate(db_name, copy_name)    
print db.list()

if raw_input('Input Y untuk menghapus database %s: ' %(db_name)) == 'Y':
    db.drop(db_name)
print db.list()
