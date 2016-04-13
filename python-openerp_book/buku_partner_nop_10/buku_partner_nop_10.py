from openerp.osv import orm


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    def onchange_buku_field_19(self, cr, uid, ids, buku_field_19, context=None):
        ret = {}
        ret['warning'] = {
                            'title': 'Pesan',
                            'message': 'Isi field buku_field_19 adalah %s' %(buku_field_19),
                          }
        return ret
    
