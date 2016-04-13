# 11_8.py
# (c) Noprianto <nop@noprianto.com> GPL
#
# Membuat laporan sederhana (PDF)

import base64
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
    report = client.get_report('res.partner', partner_search)
    report_result = report.get()
    if report_result:
        fout = '/tmp/report.pdf'
        f = open(fout, 'wb')
        f.write(base64.decodestring(report_result))
        f.close()
        print 'Laporan disimpan pada %s' %(fout)
    else:
        print 'Laporan gagal dihasilkan'
else:
    print 'Laporan tidak dibuat'
