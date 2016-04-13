from openerp.osv import orm, fields


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
                    'buku_field_9': fields.char('Buku Field 9', size=20, readonly=True), 
                    'buku_field_10': fields.char('Buku Field 10'),
                }
    
    _defaults = {
                 'buku_field_9': 'Contoh default',
                 'buku_field_10': lambda self, cr, uid, context: ' '.join(context.keys()),
                 }

