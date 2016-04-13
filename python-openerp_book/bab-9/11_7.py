# 11_7.py
# (c) Noprianto <nop@noprianto.com> GPL
#
# Mencari partner

import oerpapi

host = 'localhost'
db_name = 'test1'
user = 'demo'
password = 'demo'

client = oerpapi.OErpClient(host)
client.connect()
version = client.version()
print 'Terhubung pada %s, versi %s' %(host, version.get('server_version'))

client.login(db_name, user, password)
print 'Login dengan UserID: %s' %(client.uid)

search_name = raw_input('Mencari nama partner yang mengandung teks berikut: ')
search_data = [('name', 'ilike', search_name)]
print search_data

partner = client.get_model('res.partner')
partner_search = partner.search(search_data)
print 'Ditemukan %s partner' %(len(partner_search))

if partner_search:
    fields = ['name']
    partner_read = partner.read(partner_search, fields)
    for i in partner_read:
        print i.get('name')
