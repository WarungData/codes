#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.

import gtk
import xfce4.netk as netk

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.set_title('Background Image')
        self.win.connect('destroy', gtk.main_quit)
        #
        self.screen = netk.screen_get_default()
        self.bgpix = self.screen.get_background_pixmap()
        #
        self.img = gtk.Image()
        self.img.set_from_pixmap(self.bgpix, None)
        #
        self.win.add(self.img)
        self.win.show_all()

if __name__ == '__main__':
    app = Main()
    gtk.main()
