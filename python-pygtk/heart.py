#!/usr/bin/env python

#Shaped Window using PyGTK
#(c) Noprianto <nop@noprianto.com>, 2009, GPL
#

import pygtk
pygtk.require('2.0')
import gtk

class Main:
    def __init__(self):
        win = gtk.Window(gtk.WINDOW_POPUP)
        win.connect('delete_event', self.delete_event)
        win.set_events(win.get_events() | gtk.gdk.BUTTON_PRESS_MASK)
        win.connect('button_press_event', self.delete_event)
        win.show()
        
        pixmap, mask = gtk.gdk.pixmap_create_from_xpm(win.window, 
                None, './heart.xpm')
        img = gtk.Image()
        img.set_from_pixmap(pixmap, mask)
        
        fix = gtk.Fixed()
        fix.put(img, 0, 0)

        win.add(fix)
        win.shape_combine_mask(mask, 0, 0)
        win.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        win.show_all()

    def delete_event(self, widget, event):
        gtk.main_quit()
        return False

if __name__ == '__main__':
    app = Main()
    gtk.main()
