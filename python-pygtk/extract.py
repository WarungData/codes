#!/usr/bin/env python

#Extract Archive
#(c) Noprianto <nop@noprianto.com>, 2009, GPL
#

import pygtk
pygtk.require('2.0')
import gtk
import tarfile as tar

class Main:
    def __init__(self):
        self.archive = ''
        self.contents = []
        self.mode = 'r'
        self.outdir = ''
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title('List/extract arsip Tar, Tar.gz, Tar.bz2')
        self.window.set_size_request(400, 200)
        self.window.connect('destroy', gtk.main_quit)
        
        self.btn_fin = gtk.Button(stock=gtk.STOCK_OPEN)
        self.btn_fin.connect('clicked', self.do_open)
        
        self.btn_dout = gtk.FileChooserButton('Pilih direktori output')
        self.btn_dout.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        
        self.btn_extract = gtk.Button('E_xtract')
        self.btn_extract.connect('clicked', self.do_extract)
        
        self.hbox1 = gtk.HBox(True)
        self.hbox1.pack_start(gtk.Label('Select archive'))
        self.hbox1.pack_start(self.btn_fin)
        
        self.hbox2 = gtk.HBox(True)
        self.hbox2.pack_start(gtk.Label('Output dir'))
        self.hbox2.pack_start(self.btn_dout)
        
        self.hbox3 = gtk.HBox(True)
        self.hbox3.pack_start(gtk.Label('Click to extract'))
        self.hbox3.pack_start(self.btn_extract)

        self.textb = gtk.TextBuffer()
        self.textv = gtk.TextView(self.textb)
        self.scrollw = gtk.ScrolledWindow()
        self.scrollw.set_policy(gtk.POLICY_AUTOMATIC,
                gtk.POLICY_AUTOMATIC)
        self.scrollw.add(self.textv)

        self.statbar = gtk.Statusbar()

        self.vbox = gtk.VBox(True)
        self.vbox.pack_start(self.hbox1)
        self.vbox.pack_start(self.hbox2)
        self.vbox.pack_start(self.hbox3)
        self.vbox.pack_start(self.scrollw)
        self.vbox.pack_start(self.statbar)
        
        self.window.add(self.vbox)
        self.window.show_all()
        
    def do_open(self, widget):
        self.archive = ''
        
        dialog = gtk.FileChooserDialog('Choose Archive', self.window,
            action=gtk.FILE_CHOOSER_ACTION_OPEN,
            buttons=(gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        
        filter_tar = gtk.FileFilter()
        filter_tar.set_name('Tarball')
        filter_tar.add_pattern('*.tar')

        filter_targz = gtk.FileFilter()
        filter_targz.set_name('Gzip Tarball')
        filter_targz.add_pattern('*.tar.gz')

        filter_tarbz2 = gtk.FileFilter()
        filter_tarbz2.set_name('Bzip2 Tarball')
        filter_tarbz2.add_pattern('*.tar.bz2')
        
        dialog.add_filter(filter_tar)
        dialog.add_filter(filter_targz)
        dialog.add_filter(filter_tarbz2)
        
        dialog.set_select_multiple(False)
        
        result = dialog.run()
        if result == gtk.RESPONSE_OK:
            filename = dialog.get_filename()
            if filename:
                self.archive = filename
                if self.archive.endswith('.tar.gz'):
                    self.mode = 'r:gz'
                elif self.archive.endswith('.tar.bz2'):
                    self.mode = 'r:bz2'
                else:
                    self.mode = 'r'
        
        dialog.destroy()
        
        tarball = tar.open(self.archive, self.mode)
        self.contents = tarball.getnames()
        tarball.close()

        text = '\n'.join(self.contents)
        self.textb.set_text(text)

        self.statbar.push(1, self.archive)
    
    def do_extract(self, widget):
        self.outdir = self.btn_dout.get_filename()

        tarball = tar.open(self.archive, self.mode)
        for f in self.contents:
            while gtk.events_pending():
                gtk.main_iteration(False)
            self.statbar.push(1, f)
            tarball.extract(f, self.outdir)
        tarball.close()

        self.statbar.push(1, 'Done')

if __name__ == '__main__':
    app = Main()
    gtk.main()
