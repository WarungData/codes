import random
from openerp.report import report_sxw


class buku_partner_nop_14(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(buku_partner_nop_14, self).__init__(cr, uid, name, context=context)
        self.localcontext.update(
                                 {
                                    'random': random,
                                  }
                                 )


report_sxw.report_sxw('report.buku.partner.nop.14', 'res.partner', 
                      'addons/buku_partner_nop_14/report.rml',
                      parser=buku_partner_nop_14)
