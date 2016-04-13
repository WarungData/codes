from openerp.osv import orm, fields


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
                    'buku_field_11': fields.char('Buku Field 11', size=20, 
                                                 required=True), 
                }
    
    _defaults = {
                    'buku_field_11': 'hello',
                 }
    
    def _check_field_11(self, cr, uid, ids, context=None):
        for i in self.browse(cr, uid, ids, context=context):
            if len(i.buku_field_11) >= 3:
                return True
        return False
    
    _constraints = (
                    [_check_field_11, 'Panjang harus minimal 3 karakter', ['buku_field_11']],
                    )
    
                    
