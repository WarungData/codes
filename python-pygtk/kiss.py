#!/usr/bin/env python

#Kiss
#(c) Noprianto <nop@noprianto.com>, 2008, GPL
#

import pygtk
pygtk.require('2.0')
import gtk

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.set_size_request(600, 400)
        self.win.set_title('Click for Kiss')
        self.win.set_resizable(False)
        self.win.set_events(
                self.win.get_events() | gtk.gdk.BUTTON_PRESS_MASK)
        self.win.connect('destroy', gtk.main_quit)
        self.win.connect('button_press_event', 
            self.show_flower)
       
        self.img_size = 64

        self.fix = gtk.Fixed()
        
        self.win.add(self.fix)

        self.win.show_all()
        
    def show_flower(self, widget, event):
        count = 0
        if event.type == gtk.gdk.BUTTON_PRESS:
            count = 1
        elif event.type == gtk.gdk._2BUTTON_PRESS:
            count = 2
        elif event.type == gtk.gdk._3BUTTON_PRESS:
            count = 3

        for i in range(count):
            img = gtk.Image()
            img.set_from_file('./face-kiss.png')
            img.show()
            x = int(event.x) + (i*self.img_size)
            y = int(event.y) 
            self.fix.put(img, x, y)

if __name__ == '__main__':
    app = Main()
    gtk.main()
