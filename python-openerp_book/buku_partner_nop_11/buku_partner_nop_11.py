from openerp.osv import orm


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    def onchange_buku_field_20(self, cr, uid, ids, buku_field_20, 
                               buku_field_19, context=None):
        ret = {}
        ret['value'] = {
                        'buku_field_20': buku_field_19,
                        'buku_field_19': buku_field_20,
                        }
        return ret
    
