from openerp.osv import orm, fields


class buku_nop_report_1(orm.TransientModel):
    _name = 'buku.nop.report.1'
    _description = 'buku nop report 1 wizard'
    
    _columns = {
                    'name': fields.char('Nama mengandung teks', size=64),
                }
    
    def _get_data(self, cr, uid, ids, context=None):
        ret = {}
        
        res = self.read(cr, uid, ids, context=context)
        if res:
            ret = res[0]

        return ret
    
    def download_pdf(self, cr, uid, ids, context=None):
        data = self._get_data(cr, uid, ids, context=context)
        
        domain = [('name', 'ilike', data.get('name'))]
        search_result = self.pool.get('res.partner').search(cr, uid, domain)
        datas = {
                    'ids': search_result,
                    'model': 'res.partner',
                    'form': data,
                 }

        ret = {
                'type': 'ir.actions.report.xml',
                'report_name': self._name,
                'datas': datas,
               }
        return ret

