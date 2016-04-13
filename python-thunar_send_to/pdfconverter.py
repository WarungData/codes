#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys
import os
import commands

class Main:
    def __init__(self):
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        win.connect('destroy', gtk.main_quit)
        win.set_title('PDF Converter')

        try:
            self.f = os.path.abspath(sys.argv[1])
            self.d = os.path.dirname(self.f)
        except IndexError:
            self.f = ''
            self.d = ''
        
        #
        frm_src = gtk.Frame('Source and working directory')
        lbl_src1 = gtk.Label('PDF File')
        lbl_src1.set_alignment(0, 0.5)
        lbl_src2 = gtk.Label(self.f)
        lbl_src2.set_alignment(0, 0.5)
        lbl_base1 = gtk.Label('Working directory')
        lbl_base1.set_alignment(0, 0.5)
        lbl_base2 = gtk.Label(self.d)
        lbl_base2.set_alignment(0, 0.5)
        hb_src = gtk.HBox(True)
        hb_src.pack_start(lbl_src1, padding=10)
        hb_src.pack_start(lbl_src2, padding=10)
        hb_base = gtk.HBox(True)
        hb_base.pack_start(lbl_base1, padding=10)
        hb_base.pack_start(lbl_base2, padding=10)
        vb_src = gtk.VBox()
        vb_src.pack_start(hb_src, padding=10)
        vb_src.pack_start(hb_base, padding=10)
        frm_src.add(vb_src)
        #
        frm_conv = gtk.Frame('Convert to')
        self.check_txt = gtk.CheckButton('Te_xt File (txt)')
        self.check_html = gtk.CheckButton('_HTML File (html)')
        self.check_ppm = gtk.CheckButton('_Portable Pixmap (ppm)')
        self.check_ps = gtk.CheckButton('Post_Script (ps)')
        vb_conv = gtk.VBox()
        vb_conv.pack_start(self.check_txt, padding=10)
        vb_conv.pack_start(self.check_html, padding=10)
        vb_conv.pack_start(self.check_ppm, padding=10)
        vb_conv.pack_start(self.check_ps, padding=10)
        frm_conv.add(vb_conv)
        #
        btn_close = gtk.Button(stock=gtk.STOCK_CLOSE)
        btn_close.connect('clicked', gtk.main_quit)
        img_conv = gtk.Image()
        img_conv.set_from_stock(gtk.STOCK_EXECUTE,
                gtk.ICON_SIZE_BUTTON)
        btn_conv = gtk.Button('Con_vert')
        btn_conv.set_image(img_conv)
        btn_conv.connect('clicked', self.do_convert)
        btnbox = gtk.HButtonBox()
        btnbox.set_layout(gtk.BUTTONBOX_END)
        btnbox.set_spacing(10)
        btnbox.pack_start(btn_close, padding=10)
        btnbox.pack_start(btn_conv, padding=10)
        #
        vb = gtk.VBox()
        vb.pack_start(frm_src, padding=10)
        vb.pack_start(frm_conv, padding=10)
        vb.pack_start(btnbox, padding=10, 
                expand=False)
        #

        win.add(vb)
        win.show_all()

    def do_convert(self, widget):
        c_txt = self.check_txt.get_active()
        c_html = self.check_html.get_active()
        c_ppm = self.check_ppm.get_active()
        c_ps = self.check_ps.get_active()

        cmds = []
        if c_txt:
            cmds.append('pdftotext %s' %(self.f))
        if c_html:
            cmds.append('pdftohtml %s' %(self.f))
        if c_ppm:
            cmds.append('pdftoppm %s %s' %(self.f, self.f))
        if c_ps:
            cmds.append('pdftops %s' %(self.f))
        
        for c in cmds:
            ret = commands.getstatusoutput(c)

if __name__ == '__main__':
    app = Main()
    gtk.main()
