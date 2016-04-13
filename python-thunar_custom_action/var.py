#!/usr/bin/env python

#(c) Noprianto, GPL.
#thunar custom action 
#get files

#custom actions
#menu: Edit -> Configure Custom Actions...
#cmd = one of ['f', 'F', 'd', 'D', 'n', 'N']
#1. add a new custom action
#2. basic: 
#   - name: Get Files <cmd>
#   - command: python <var.py> <cmd>
#3. appearance conditions
#   - file pattern: *
#   -> check all on 'Appears if selection contains'

import sys
import gtk

cmds = ['f', 'F', 'd', 'D', 'n', 'N']

def show(title, files):
    win = gtk.Window()
    win.connect('destroy', gtk.main_quit)
    win.set_title(title)
    #
    lstore = gtk.ListStore(str)
    #
    treev = gtk.TreeView(lstore)
    treev.set_size_request(400, 400)
    #
    tvcol = gtk.TreeViewColumn('Files')
    cell = gtk.CellRendererText()
    tvcol.pack_start(cell, True)
    tvcol.set_attributes(cell, text=0)
    treev.append_column(tvcol)
    #
    for f in files:
        lstore.append([f])
    #
    scrollw = gtk.ScrolledWindow()
    scrollw.set_policy(gtk.POLICY_AUTOMATIC, 
        gtk.POLICY_AUTOMATIC)
    scrollw.add(treev)
    #
    win.add(scrollw)
    win.show_all()
    #
    gtk.main()
    
def main(cmd, args):
    if not cmd in cmds:
        return
    #
    msg = ''
    if cmd == 'f':
        msg = 'First selected file'
    elif cmd == 'F':
        msg = 'Selected files'
    elif cmd == 'd':
        msg = 'Directory of first selected file'
    elif cmd == 'D':
        msg = 'Directories of selected files'
    elif cmd == 'n':
        msg = 'First selected file name (without path)'
    elif cmd == 'N':
        msg = 'Selected file names (without path)'
    #
    tmp = frozenset(args)
    show(msg, tmp)

#
if __name__ == '__main__':
    if not len(sys.argv) > 2:
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2:])
    
