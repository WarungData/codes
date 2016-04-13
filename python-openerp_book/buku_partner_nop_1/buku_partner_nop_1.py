from openerp.osv import orm, fields


SELECTION_1 = [
               ('pilihan1', 'Pilihan 1'),
               ('pilihan2', 'Pilihan 2'),
               ('pilihan3', 'Pilihan 3'),
               ]

SELECTION_2 = [
               ('pilihan4', 'Pilihan 4'),
               ('pilihan5', 'Pilihan 5'),
               ('pilihan6', 'Pilihan 6'),
               ('pilihan7', 'Pilihan 7'),
               ('pilihan8', 'Pilihan 8'),
               ('pilihan9', 'Pilihan 9'),
               ('pilihan10', 'Pilihan 10'),
               ]


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    def _get_selection_2(self, cr, uid, context=None):
        return SELECTION_2
    
    _columns = {
                    'buku_field_1': fields.char('Buku Field 1', size=20, 
                                                required=True, 
                                                help='Contoh help'),
                    'buku_field_2': fields.float('Buku Field 2', digits=(4, 2)),
                    'buku_field_3': fields.integer('Buku Field 3', size=10),
                    'buku_field_4': fields.boolean('Buku Field 4'),
                    'buku_field_5': fields.date('Buku Field 5'),
                    'buku_field_6': fields.datetime('Buku Field 6'),
                    'buku_field_7': fields.selection(SELECTION_1, 'Buku Field 7'),
                    'buku_field_8': fields.selection(_get_selection_2, 'Buku Field 8'),
                }

