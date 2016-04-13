#!/usr/bin/env python

#Simple Animation
#(c) Noprianto <nop@noprianto.com>, 2009, GPL
#


import pygtk
pygtk.require('2.0')
import gtk
import gobject

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.connect('destroy', self.main_quit)
        self.win.set_size_request(600, 400)
        self.win.set_resizable(False)
        self.win.set_title('Simple Animation')

        self.img = gtk.Image()
        self.img.set_from_file('./heart-small.xpm')

        self.posx = 20
        self.posy = 20
        self.dx = 1
        self.dy = 1
        self.fix = gtk.Fixed()
        self.fix.put(self.img, self.posx, self.posy)

        self.win.add(self.fix)
        self.win.show_all()
    
        self.id = gobject.timeout_add(10, self.do_anim)

    def main_quit(self, param):
        gobject.source_remove(self.id)
        gtk.main_quit()

    def do_anim(self):
        if self.posx > 520 or self.posx < 20:
            self.dx *= -1
        
        if self.posy > 320 or self.posy < 20:
            self.dy *= -1

        self.posx += self.dx
        self.posy += self.dy
            
        self.fix.move(self.img, self.posx, self.posy)
        return True

if __name__ == '__main__':
    app = Main()
    gtk.main()


