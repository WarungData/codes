from openerp.report import report_sxw


class buku_nop_report_1(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(buku_nop_report_1, self).__init__(cr, uid, name, context=context)


report_sxw.report_sxw('report.buku.nop.report.1', 'res.partner', 
                      'addons/buku_nop_report_1/report.rml',
                      parser=buku_nop_report_1)

