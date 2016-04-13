#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import gtk
import xfce4.gui as gui
import xfce4.util as util

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('About')
        #
        self.btn_about = gtk.Button(stock=gtk.STOCK_ABOUT)
        self.btn_about.connect('clicked', self.show_about)
        #
        self.win.add(self.btn_about)
        self.win.show_all()
        #
    
    def show_about(self, widget):
        d = gui.AboutDialog()
        #
        d.set_copyright('(c) Noprianto, 2009')
        d.set_description('Do-nothing program, eat your resources')
        d.set_homepage('http://noprianto.com')
        d.set_license(util.LICENSE_BSD)
        d.set_program('gui3.py')
        d.set_version('0.0.0')
        #
        d.add_credit('Noprianto','nop@sent.com', 'Main Developer')
        d.add_credit('Chinmi','kungfu boy', 'Main Tester')
        #
        d.show_all()
        #
        d.run()
        d.destroy()

        
if __name__ == '__main__':
    app = Main()
    gtk.main()

