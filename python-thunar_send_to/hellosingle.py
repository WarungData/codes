#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys

class Main:
    def __init__(self):
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        win.connect('destroy', gtk.main_quit)
        win.set_title('Hello Single')

        try:
            f = sys.argv[1]
        except IndexError:
            f = ''
        lbl = gtk.Label(f)
        lbl.set_size_request(320, 100)

        win.add(lbl)
        win.show_all()

if __name__ == '__main__':
    app = Main()
    gtk.main()
