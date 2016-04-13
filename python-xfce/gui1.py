#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import gtk
import xfce4.gui as gui

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('Xfce Dialogs')
        #
        self.btn_info = gtk.Button(stock=gtk.STOCK_DIALOG_INFO)
        self.btn_info.connect('clicked', self.show_info)
        self.btn_warning = gtk.Button(stock=gtk.STOCK_DIALOG_WARNING)
        self.btn_warning.connect('clicked', self.show_warning)
        self.btn_error = gtk.Button(stock=gtk.STOCK_DIALOG_ERROR)
        self.btn_error.connect('clicked', self.show_error)
        self.btn_confirm= gtk.Button(stock=gtk.STOCK_DIALOG_QUESTION)
        self.btn_confirm.connect('clicked', self.ask_question)
        #
        self.buttonbox = gtk.VButtonBox()
        self.buttonbox.set_spacing(10)
        self.buttonbox.pack_start(self.btn_info)
        self.buttonbox.pack_start(self.btn_warning)
        self.buttonbox.pack_start(self.btn_error)
        self.buttonbox.pack_start(self.btn_confirm)
        #
        self.win.add(self.buttonbox)
        self.win.show_all()
    
    def show_info(self, widget):
        gui.show_info('Your partition table will be destroyed soon')

    def show_warning(self, widget):
        gui.show_warning('This is warning from virus')

    def show_error(self, widget):
        gui.show_error('Fatal error occured')

    def ask_question(self, widget):
        res = gui.confirm(
            'Are you sure you want to destroy partition table?',
            gtk.STOCK_DIALOG_QUESTION, "I don't care")
        if res:
            self.show_info(widget)
        else:
            self.show_error(widget)
            

if __name__ == '__main__':
    app = Main()
    gtk.main()
