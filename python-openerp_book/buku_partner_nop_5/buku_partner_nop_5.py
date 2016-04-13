from openerp.osv import orm, fields


class res_partner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def write(self, cr, user, ids, vals, context=None):
        comment = vals.get('comment', '')
        try:
            comment = comment.strip()
            vals['comment'] = comment
        except AttributeError:
            pass
        
        return super(res_partner, self).write(cr, user, ids, vals, context)
    
    def create(self, cr, user, vals, context=None):
        comment = vals.get('comment', '')
        try:
            comment = comment.strip()
            vals['comment'] = comment
        except AttributeError:
            pass
        
        return super(res_partner, self).create(cr, user, vals, context)
    
