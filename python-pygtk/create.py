#!/usr/bin/env python

#Create Archive
#(c) Noprianto <nop@noprianto.com>, 2009, GPL
#

import pygtk
pygtk.require('2.0')
import gtk
import tarfile as tar

class Main:
    def __init__(self):
        self.outfile = ''
        self.contents = []
        self.mode = 'w'
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title('Create Archive Tar, Tar.gz, Tar.bz2')
        self.window.set_size_request(400, 100)
        self.window.connect('destroy', gtk.main_quit)
        
        self.btn_fout = gtk.Button(stock=gtk.STOCK_SAVE)
        self.btn_fout.connect('clicked', self.do_create)
        self.btn_content = gtk.Button(stock=gtk.STOCK_OPEN)
        self.btn_content.connect('clicked', self.do_add)
        
        self.hbox1 = gtk.HBox(True)
        self.hbox1.pack_start(gtk.Label('Output'))
        self.hbox1.pack_start(self.btn_fout)

        self.hbox2 = gtk.HBox(True)
        self.hbox2.pack_start(gtk.Label('Contents'))
        self.hbox2.pack_start(self.btn_content)        
        
        self.statbar = gtk.Statusbar()
        
        self.vbox = gtk.VBox(True)
        self.vbox.pack_start(self.hbox1)
        self.vbox.pack_start(self.hbox2)
        self.vbox.pack_start(self.statbar)
        
        self.window.add(self.vbox)
        self.window.show_all()
        
    def do_create(self, widget):
        self.outfile = ''
        
        dialog = gtk.FileChooserDialog('Archive Name', self.window,
            action=gtk.FILE_CHOOSER_ACTION_SAVE, 
            buttons=(gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        
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
                self.outfile = filename
                if self.outfile.endswith('.tar.gz'):
                    self.mode = 'w:gz'
                elif self.outfile.endswith('.tar.bz2'):
                    self.mode = 'w:bz2'
                else:
                    self.mode = 'w'
        
        self.statbar.push(1, self.outfile)
        
        dialog.destroy()
    
    def do_add(self, widget):
        self.contents = []
        
        dialog = gtk.FileChooserDialog('Archive Contents', self.window,
            action=gtk.FILE_CHOOSER_ACTION_OPEN, 
            buttons=(gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        
        filter_all = gtk.FileFilter()
        filter_all.set_name('All files')
        filter_all.add_pattern('*')
        
        dialog.set_select_multiple(True)

        dialog.add_filter(filter_all)
        
        result = dialog.run()
        if result == gtk.RESPONSE_OK:
            filenames = dialog.get_filenames()
            if filenames:
                self.contents = filenames
        
        dialog.destroy()
        self.statbar.push(1, 'Creating archive...')
        
        tarball = tar.open(self.outfile, self.mode)
        for f in self.contents:
            try:
                tarball.add(f)
            except IOError:
                print 'Error processing: %s' %(f)
                continue
            while gtk.events_pending():
                gtk.main_iteration(False)
            self.statbar.push(1, f)
        tarball.close()

        self.statbar.push(1, 'Done')


if __name__ == '__main__':
    app = Main()
    gtk.main()
