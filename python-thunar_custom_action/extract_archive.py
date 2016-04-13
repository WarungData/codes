#!/usr/bin/env python

#(c) Noprianto, GPL.
#thunar custom action 
#extract tar archive

#custom actions
#menu: Edit -> Configure Custom Actions...
#1. add a new custom action
#2. basic: 
#   - name: Extract Archive
#   - command: python <extract_archive.py> %f
#3. appearance conditions
#   - file pattern: *.tar; *.tar.gz; *.tgz; *.tar.bz2; *.tbz2
#   - Appears if selection contains: Other files
#      

import sys
import gtk
import tarfile

class ArchiveExtract:
    def __init__(self, archive):
        #vars
        self.archive = archive
        self.mode = 'r'
        self.dout = ''
        #
        #main window
        self.win = gtk.Window()
        self.win.connect('destroy', gtk.main_quit)
        self.win.set_title('Extract archive')
        #
        #file chooser
        self.btn_out = gtk.FileChooserButton('Select output directory')
        self.btn_out.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        #
        #action and progress bar
        self.hb_action = gtk.HBox()
        self.pbar = gtk.ProgressBar()
        self.btn_exec = gtk.Button('_Extract archive')
        self.btn_exec.connect('clicked', self.extract_archive)
        self.hb_action.pack_start(self.btn_exec, expand=False, padding=4)
        self.hb_action.pack_start(self.pbar, expand=True, padding=4)
        #
        #main
        self.vb = gtk.VBox()
        self.vb.pack_start(self.btn_out, expand=False, padding=4)
        self.vb.pack_start(self.hb_action, expand=False, padding=4)
        self.win.add(self.vb)
        #
        self.win.show_all()
        #
    
    def extract_archive(self, widget):
        self.dout = self.btn_out.get_filename()
        if not self.dout:
            return
        #
        if self.dout.endswith('.tar.gz'):
            self.mode = 'r:gz'
        elif self.dout.endswith('.tar.bz2'):
            self.mode = 'r:bz2'
        else:
            self.mode = 'r'
        #
        pos = 0.0
        self.pbar.set_fraction(pos)
        self.pbar.set_text('')    
        #
        tar = tarfile.open(self.archive, self.mode)
        contents = tar.getnames()
        frac = 1.0/len(contents)
        for f in contents:
            try:
                tar.extract(f, self.dout)
            except:
                print 'Error processing %s' %(f)
                pos += frac
                continue
            while gtk.events_pending():
                gtk.main_iteration(False)
            pos = self.pbar.get_fraction()
            pos += frac
            if pos > 1.0: pos = 1.0
            self.pbar.set_fraction(pos)
        tar.close()
        self.pbar.set_fraction(1.0)
        self.pbar.set_text('Done')    

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        sys.exit(1)
    else:
        arc = sys.argv[1]
        app = ArchiveExtract(arc)
        gtk.main()
    
