#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import gtk
import xfce4.netk as netk

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.set_size_request(300, -1)
        self.win.connect('destroy', gtk.main_quit)
        #
        pager = netk.Pager(netk.screen_get_default())
        #
        self.win.add(pager)
        self.win.show_all()
        

if __name__ == '__main__':
    app = Main()
    gtk.main()
