#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import gtk
import xfce4.gui as gui

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('Titled Dialog')
        #
        self.btn_show = gtk.Button('SHOW')
        self.btn_show.connect('clicked', self.show_dialog)
        #
        self.win.add(self.btn_show)
        self.win.show_all()
        #
    
    def show_dialog(self, widget):
        d = gui.TitledDialog()
        #
        d.set_title('Titled Dialog')
        d.set_subtitle('This is subtitle')
        #
        textb = gtk.TextBuffer()
        textv = gtk.TextView(textb)
        textb.set_text('line1\nline2\nline3')
        scrollw = gtk.ScrolledWindow()
        scrollw.set_policy(gtk.POLICY_AUTOMATIC,
            gtk.POLICY_AUTOMATIC)
        scrollw.add(textv)
        #
        d.vbox.pack_start(scrollw)
        #
        d.add_button(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT)
        d.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        #
        d.show_all()
        #
        res = d.run()
        if res == gtk.RESPONSE_ACCEPT:
            gui.show_info('OK')
        d.destroy()

        
if __name__ == '__main__':
    app = Main()
    gtk.main()


