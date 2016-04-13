#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import sys
import gtk
import xfce4.gui as gui
import xfce4.util as util

class Main:
    def __init__(self, desktop_files):
        self.desktop_files = desktop_files
        #
        self.win = gtk.Window()
        self.win.set_title('App Menu Item')
        self.win.set_size_request(100, 100)
        self.win.connect('destroy', gtk.main_quit)
        #
        self.menubar = gtk.MenuBar()
        self.menu_app = gtk.Menu()
        self.item_app = gtk.MenuItem('_Applications')
        self.item_app.set_submenu(self.menu_app)
        self.menubar.append(self.item_app)
        #
        self.keys = ['Type', 'URL', 'Exec', 'Name', 'Icon']
        self.desktop_items = []
        self.build_menus()
        #
        self.win.add(self.menubar)
        self.win.show_all()
    
    
    def build_menus(self):
        for f in self.desktop_files:
            entry = util.desktop_entry_new(f, self.keys)
            app = gui.app_menu_item_new_from_desktop_entry(entry, True)
            self.desktop_items.append(app)
        #
        for a in self.desktop_items:
            self.menu_app.append(a)
        #
        
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('%s <desktop_entry_file> [desktop_entry_file]...' 
            %(sys.argv[0]))
    else:
        desktop_files = sys.argv[1:]
        app = Main(desktop_files)
        gtk.main()
