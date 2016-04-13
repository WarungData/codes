#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import gtk
import xfce4.netk as netk

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('Windows')
        #
        self.btn_min_all = gtk.Button('Minimize all')
        self.btn_min_all.connect('clicked', self.do_windows, 
            'min_all')
        self.btn_unmin_all = gtk.Button('Un-minimize all')
        self.btn_unmin_all.connect('clicked', self.do_windows, 
            'un_min_all')
        self.btn_maxh_all = gtk.Button('Maximize horizontally all')
        self.btn_maxh_all.connect('clicked', self.do_windows, 
            'maxh_all')
        self.btn_maxv_all = gtk.Button('Maximize vertically all')
        self.btn_maxv_all.connect('clicked', self.do_windows, 
            'maxv_all')
        self.btn_shade_all = gtk.Button('Shade all')
        self.btn_shade_all.connect('clicked', self.do_windows, 
            'shade_all')
        self.btn_unshade_all = gtk.Button('Un-shade all')
        self.btn_unshade_all.connect('clicked', self.do_windows, 
            'un_shade_all')
        #
        self.buttonbox = gtk.VButtonBox()
        self.buttonbox.set_spacing(10)
        self.buttonbox.pack_start(self.btn_min_all)
        self.buttonbox.pack_start(self.btn_unmin_all)
        self.buttonbox.pack_start(self.btn_maxh_all)
        self.buttonbox.pack_start(self.btn_maxv_all)
        self.buttonbox.pack_start(self.btn_shade_all)
        self.buttonbox.pack_start(self.btn_unshade_all)
        #
        self.win.add(self.buttonbox)
        self.win.show_all()
        #
        self.screen = netk.screen_get_default()
    
    def do_windows(self, widget, action):
        self.windows = self.screen.get_windows()        
        if action == 'min_all':
            r = [x.minimize() for x in self.windows]
        elif action == 'un_min_all':
            r = [x.unminimize() for x in self.windows]
        elif action == 'maxh_all':
            r = [x.maximize_horizontally() for x in self.windows]
        elif action == 'maxv_all':
            r = [x.maximize_vertically() for x in self.windows]
        elif action == 'shade_all':
            r = [x.shade() for x in self.windows]
        elif action == 'un_shade_all':
            r = [x.unshade() for x in self.windows]
        
if __name__ == '__main__':
    app = Main()
    gtk.main()

