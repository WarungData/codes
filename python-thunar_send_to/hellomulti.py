#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys

class Main:
    def __init__(self):
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        win.connect('destroy', gtk.main_quit)
        win.set_title('Hello Multi')

        try:
            f = sys.argv[1:]
        except IndexError:
            f = []
        lstore = gtk.ListStore(str)
        trview = gtk.TreeView(lstore)
        trview.set_size_request(320, 240)
        cell = gtk.CellRendererText()
        tvcolumn = gtk.TreeViewColumn('Nama File')
        tvcolumn.pack_start(cell)
        tvcolumn.set_attributes(cell, text=0)
        trview.append_column(tvcolumn)
        #
        scrollw = gtk.ScrolledWindow()
        scrollw.set_policy(gtk.POLICY_AUTOMATIC, 
            gtk.POLICY_AUTOMATIC)
        scrollw.add(trview)

        #
        for i in f:
            lstore.append([i])

        win.add(scrollw)
        win.show_all()

if __name__ == '__main__':
    app = Main()
    gtk.main()
