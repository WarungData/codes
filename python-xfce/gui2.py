#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.
#

import gtk
import xfce4.gui as gui

class Main:
    def __init__(self):
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('Clock')
        #
        self.btn_analog = gtk.Button('_Analog')
        self.btn_analog.connect('clicked', 
            self.set_clock_mode, gui.CLOCK_ANALOG)
        self.btn_digital = gtk.Button('_Digital')
        self.btn_digital.connect('clicked', 
            self.set_clock_mode, gui.CLOCK_DIGITAL)
        self.btn_led = gtk.Button('_LED')
        self.btn_led.connect('clicked', 
            self.set_clock_mode, gui.CLOCK_LEDS)
        #
        self.buttonbox = gtk.HButtonBox()
        self.buttonbox.set_spacing(10)
        self.buttonbox.pack_start(self.btn_analog)
        self.buttonbox.pack_start(self.btn_digital)
        self.buttonbox.pack_start(self.btn_led)
        #
        self.clock = gui.Clock()
        self.clock.set_size_request(300, 300)
        #
        self.vbox = gtk.VBox()
        self.vbox.pack_start(self.buttonbox, expand=False)
        self.vbox.pack_start(self.clock)
        #
        self.win.add(self.vbox)
        self.win.show_all()
        #
    
    def set_clock_mode(self, widget, mode):
        self.clock.set_mode(mode)

        
if __name__ == '__main__':
    app = Main()
    gtk.main()

