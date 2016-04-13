#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys
import commands
import stat
import os

class Main:
    def __init__(self):
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        win.connect('destroy', gtk.main_quit)
        win.set_title('Shredder')

        try:
            f = []
            a = sys.argv[1:]
            for i in a:
                if os.path.exists(i):
                    #regular file only
                    mode = os.stat(i)[stat.ST_MODE]
                    if stat.S_ISREG(mode):
                        f.append(i)
        except IndexError:
            f = []

        #
        lstore = gtk.ListStore(str)
        trview = gtk.TreeView(lstore)
        trview.set_size_request(320, 240)
        cell = gtk.CellRendererText()
        tvcolumn = gtk.TreeViewColumn('Files')
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
        #
        statb = gtk.Statusbar()
        #
        btn_close = gtk.Button(stock=gtk.STOCK_CLOSE)
        btn_close.connect('clicked', gtk.main_quit)
        #
        img_shred = gtk.Image()
        img_shred.set_from_stock(gtk.STOCK_EXECUTE,
                gtk.ICON_SIZE_BUTTON)
        btn_shred = gtk.Button('_Shred All')
        btn_shred.set_image(img_shred)
        btn_shred.connect('clicked', self.do_shred, 
                lstore, statb)
        #
        btnbox = gtk.HButtonBox()
        btnbox.set_layout(gtk.BUTTONBOX_END)
        btnbox.set_spacing(10)
        btnbox.pack_start(btn_close, padding=10)
        btnbox.pack_start(btn_shred, padding=10)
        #
        vb = gtk.VBox()
        vb.pack_start(scrollw, padding=10)
        vb.pack_start(btnbox, padding=10, 
                expand=False)
        vb.pack_start(statb, expand=False)
        #
    
        win.add(vb)
        win.show_all()
    
    def do_shred(self, widget, model, statb):
        files = []
        iter = model.get_iter_first()
        while iter:
            f = model.get_value(iter, 0)
            files.append(f)
            iter = model.iter_next(iter) 
        #
        failed = []
        for f in files:
            cmd = 'shred -u "%s"' %(f)
            statb.push(1, 'Shredding %s' %(f))
            ret = commands.getstatusoutput(cmd)
            if ret[0] != 0:
                failed.append(f)
            while gtk.events_pending():
                gtk.main_iteration(False)
        #
        if not failed:
            statb.push(1, 'All done.')
        else:
            statb.push(1, '%s failed.' %(len(failed)))
        #
        model.clear()
        for f in failed:
            model.append([f])
                


if __name__ == '__main__':
    app = Main()
    gtk.main()
