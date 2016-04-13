from openerp.osv import orm, fields


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
        
    _columns = {
                    'buku_field_13': fields.char('Buku Field 13', size=10),
                    'buku_field_14': fields.char('Buku Field 14', size=10),
                    'buku_field_15': fields.char('Buku Field 15', size=10),
                    'buku_field_16': fields.char('Buku Field 16', size=10),
                    'buku_field_17': fields.char('Buku Field 17', size=10),
                    'buku_field_18': fields.char('Buku Field 18', size=10),
                    'buku_field_19': fields.char('Buku Field 19', size=10),
                    'buku_field_20': fields.char('Buku Field 20', size=10),
                }

