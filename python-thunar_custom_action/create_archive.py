#!/usr/bin/env python

#(c) Noprianto, GPL.
#thunar custom action 
#create tar archive

#custom actions
#menu: Edit -> Configure Custom Actions...
#1. add a new custom action
#2. basic: 
#   - name: Create Archive
#   - command: python <create_archive.py> %F
#3. appearance conditions
#   - file pattern: *
#   -> check all on 'Appears if selection contains', except
#      Directories

import sys
import gtk
import tarfile

class ArchiveCreate:
    def __init__(self, files):
        #vars
        self.files = files
        self.mode = 'w'
        self.fout = ''
        #
        #main window
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('Create archive')
        #
        #file chooser
        self.btn_out = gtk.Button('Archive name')
        self.btn_out.connect('clicked', self.get_filename)
        #
        #treeview
        self.lstore = gtk.ListStore(str)
        self.treev = gtk.TreeView(self.lstore)
        self.treev.set_size_request(400, 400)
        self.tvcol = gtk.TreeViewColumn('Files')
        self.cell = gtk.CellRendererText()
        self.tvcol.pack_start(self.cell, True)
        self.tvcol.set_attributes(self.cell, text=0)
        self.treev.append_column(self.tvcol)
        self.scrollw = gtk.ScrolledWindow()
        self.scrollw.set_policy(gtk.POLICY_AUTOMATIC, 
            gtk.POLICY_AUTOMATIC)
        self.scrollw.add(self.treev)
        #
        #action and progress bar
        self.hb_action = gtk.HBox()
        self.pbar = gtk.ProgressBar()
        self.btn_exec = gtk.Button('_Create archive')
        self.btn_exec.connect('clicked', self.create_archive)
        self.hb_action.pack_start(self.btn_exec, expand=False, padding=4)
        self.hb_action.pack_start(self.pbar, expand=True, padding=4)
        #
        #main
        self.vb = gtk.VBox()
        self.vb.pack_start(self.btn_out, expand=False, padding=4)
        self.vb.pack_start(self.scrollw, expand=True, padding=4)
        self.vb.pack_start(self.hb_action, expand=False, padding=4)
        self.win.add(self.vb)
        #
        self.list_files()
        #
        self.win.show_all()
        #

    def list_files(self):
        for f in self.files:
            self.lstore.append([f])
        
    def get_filename(self, widget):
        dialog = gtk.FileChooserDialog('Enter archive name', self.win,
                action=gtk.FILE_CHOOSER_ACTION_SAVE, 
                buttons=(gtk.STOCK_SAVE, gtk.RESPONSE_OK))

        filter_tar = gtk.FileFilter()
        filter_tar.set_name('Tarball')
        filter_tar.add_pattern('*.tar')
        #
        filter_targz = gtk.FileFilter()
        filter_targz.set_name('Gzip Tarball')
        filter_targz.add_pattern('*.tar.gz')
        #
        filter_tarbz2 = gtk.FileFilter()
        filter_tarbz2.set_name('Bzip2 Tarball')
        filter_tarbz2.add_pattern('*.tar.bz2')
        #
        dialog.add_filter(filter_tar)
        dialog.add_filter(filter_targz)
        dialog.add_filter(filter_tarbz2)
        #
        res = dialog.run()
        if res == gtk.RESPONSE_OK:
            self.fout = dialog.get_filename()
            if self.fout.endswith('.tar.gz'):
                self.mode = 'w:gz'
            elif self.fout.endswith('.tar.bz2'):
                self.mode = 'w:bz2'
            else:
                self.mode = 'w'
        dialog.destroy()
        #
        if self.fout:
            widget.set_label(self.fout)
    

    def create_archive(self, widget):
        if not self.fout:
            return
        #
        frac = 1.0/len(self.files)
        pos = 0.0
        self.pbar.set_fraction(pos)
        self.pbar.set_text('')    
        #
        tar = tarfile.open(self.fout, self.mode)
        for f in self.files:
            try:
                tar.add(f)
            except:
                print 'Error processing %s' %(f)
                pos += frac
                continue
            while gtk.events_pending():
                gtk.main_iteration(False)
            pos = self.pbar.get_fraction()
            pos += frac
            self.pbar.set_fraction(pos)
        tar.close()
        self.pbar.set_fraction(1.0)
        self.pbar.set_text('Done')
    

    

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        sys.exit(1)
    else:
        files = sys.argv[1:]
        app = ArchiveCreate(files)
        gtk.main()
    
