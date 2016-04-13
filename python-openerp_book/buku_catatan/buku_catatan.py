from openerp.osv import orm, fields


class res_partner(orm.Model):
    _name = 'buku.catatan'
    _description = 'Catatan'
        
    _columns = {
                    'title': fields.char('Title', size=32, required=True),
                    'content': fields.text('Content'),
                }

