# 11_6.py
# (c) Noprianto <nop@noprianto.com> GPL
#
# Membuat partner baru
# Mengupdate data partner 
# Menampilkan data partner 
# Menghapus partner

import oerpapi

host = 'localhost'
db_name = 'test1'
user = 'demo'
password = 'demo'

fields = ['name', 'website']

client = oerpapi.OErpClient(host)
client.connect()
version = client.version()
print 'Terhubung pada %s, versi %s' %(host, version.get('server_version'))

client.login(db_name, user, password)
print 'Login dengan UserID: %s' %(client.uid)

print 'Membuat partner (res.partner) baru'
partner_data = {}
for f in fields:
    temp = raw_input('%s: ' %(f))
    partner_data[f] = temp
partner = client.get_model('res.partner')
partner_id = partner.create(partner_data)
print 'Partner ID adalah %s' %(partner_id)

print 'Mengupdate data partner ID %s' %(partner_id)
partner_data = {}
for f in fields:
    temp = raw_input('%s: ' %(f))
    partner_data[f] = temp
partner.write(partner_id, partner_data)

print 'Menampilkan data partner ID %s' %(partner_id)
partner_read = partner.read(partner_id, fields)
print partner_read

if raw_input('Input Y untuk menghapus partner ID %s: ' %(partner_id)) == 'Y':
    partner.unlink(partner_id)
