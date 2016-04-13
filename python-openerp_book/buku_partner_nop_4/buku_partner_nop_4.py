import random
from openerp.osv import orm, fields


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    def _function_test(self, cr, uid, ids, field, arg, context=None):
        res = {}
        for i in ids:
            res[i]  = random.random()
        return res
    
    _columns = {
                    'buku_field_12': fields.function(_function_test, type='float') 
                }
        
    
