#!/usr/bin/env python

#Tips Of The Day
#(c) Noprianto <nop@noprianto.com>, 2009, GPL
#

import pygtk
pygtk.require('2.0')
import gtk

class Main:
    def __init__(self):
        self.file = './tips.txt'
        self.data = open(self.file).readlines()
        self.index = 0  #tips index
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title('Tips of the Day')
        self.window.set_size_request(400, 200)
        self.window.set_resizable(False)
        self.window.connect('destroy', gtk.main_quit)
        
        self.image = gtk.Image()
        self.image.set_from_stock(gtk.STOCK_DIALOG_INFO, 
                gtk.ICON_SIZE_LARGE_TOOLBAR)

        self.label = gtk.Label()
        self.label.set_markup('<b>Tips of the Day</b>')

        self.textb = gtk.TextBuffer()
        self.textb.set_text(self.data[self.index])
        self.textv = gtk.TextView(self.textb)
        self.textv.set_editable(False)
        self.textv.set_cursor_visible(False)
        self.textv.set_wrap_mode(gtk.WRAP_CHAR)
        self.scrollw = gtk.ScrolledWindow()
        self.scrollw.set_policy(gtk.POLICY_AUTOMATIC,
                gtk.POLICY_AUTOMATIC)
        self.scrollw.add(self.textv)

        self.btn_prev = gtk.Button(stock=gtk.STOCK_MEDIA_PREVIOUS)
        self.btn_prev.connect('clicked', self.show_tips, 'prev')
        self.btn_next = gtk.Button(stock=gtk.STOCK_MEDIA_NEXT)
        self.btn_next.connect('clicked', self.show_tips, 'next')

        self.btnbox = gtk.HButtonBox()
        self.btnbox.set_layout(gtk.BUTTONBOX_END)
        self.btnbox.set_spacing(10)
        self.btnbox.pack_start(self.btn_prev)
        self.btnbox.pack_start(self.btn_next)
            
        self.table = gtk.Table(5, 10, True)
        self.table.attach(self.image, 0, 1, 0, 1)
        self.table.attach(self.label, 0, 10, 0, 1)
        self.table.attach(self.scrollw, 0, 10, 1, 4)
        self.table.attach(self.btnbox, 0, 10, 4, 5)
        
        self.window.add(self.table)
        self.window.show_all()
    
    def show_tips(self, widget, action):
        if action == 'prev':
            if self.index > 0:
                self.index -= 1
        elif action == 'next':
            if self.index < len(self.data) - 1:
                self.index += 1            
        else:
            self.index = 0
            
        text = self.data[self.index].strip()
        if text:
            self.textb.set_text(text)

        
if __name__ == '__main__':
    app = Main()
    gtk.main()
