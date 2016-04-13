#!/usr/bin/env python

#Simple Audio Player
#based on gtk+ and pygame
#(c) Noprianto <nop@noprianto.com>, 2009, GPL
#

import os
import gtk
import gobject
import pygame

class SqliteDB:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.engine = None
        #
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                pass
        #
        if sqlite3:
            self.engine = sqlite3
        #
        
    def query(self, query, args):
        if not self.engine:
            return [1, 'Database Engine not specified']
        #
        ret_data = []
        ret = []
        try:
            conn = self.engine.connect(self.dbfile)
            cur = conn.cursor()
            cur.execute(query, args)
            ret_data = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            ret = [0, ret_data, cur.lastrowid]
        except Exception, e:
            ret = [2, e.message, None]
        #
        return ret
    
    def getsize(self):
        try:
            size = os.path.getsize(self.dbfile)
        except:
            size = 0
        return size
            

class Main:
    def __init__(self):
        #
        self.db = SqliteDB('audio_player.db')
        if self.db.getsize() == 0:
            self.initdb()        
        #
        pygame.mixer.init()
        pygame.display.init()
        self.pos = 0
        self.length = 0
        #
        self.win = gtk.Window()
        self.win.set_title('Simple Audio Player')
        self.win.connect('destroy', gtk.main_quit)
        #
        self.lstore = gtk.ListStore(str)
        self.treev = gtk.TreeView(self.lstore)
        self.treev.set_size_request(400, 300)
        self.tvcol = gtk.TreeViewColumn('Audio File')
        self.cell = gtk.CellRendererText()
        self.tvcol.pack_start(self.cell, True)
        self.tvcol.set_attributes(self.cell, text=0)
        self.treev.append_column(self.tvcol)
        self.treev.connect('row-activated', self.select_song)
        #
        self.scroll_song = gtk.ScrolledWindow()
        self.scroll_song.set_policy(
            gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.scroll_song.add(self.treev)
        #
        self.fch = gtk.FileChooserButton('Select Play List')
        #
        self.lbl_list = gtk.Label('Playlist')
        #
        self.btn_load = gtk.Button(stock=gtk.STOCK_OPEN)
        self.btn_load.connect('clicked', self.load_songs)
        #
        self.hbox_song = gtk.HBox()
        self.hbox_song.set_spacing(10)
        self.hbox_song.pack_start(self.lbl_list, expand=False)
        self.hbox_song.pack_start(self.fch, expand=True)
        self.hbox_song.pack_start(self.btn_load, expand=False)
        #
        self.btn_play = gtk.ToolButton(gtk.STOCK_MEDIA_PLAY)
        self.btn_play.connect('clicked', self.play_song)
        self.btn_stop = gtk.ToolButton(gtk.STOCK_MEDIA_STOP)
        self.btn_stop.connect('clicked', self.stop_song)
        #
        self.btnbox_song = gtk.HButtonBox()
        self.btnbox_song.set_spacing(10)
        self.btnbox_song.set_layout(gtk.BUTTONBOX_SPREAD)
        self.btnbox_song.pack_start(self.btn_play)
        self.btnbox_song.pack_start(self.btn_stop)
        #
        self.vbox_song = gtk.VBox()
        self.vbox_song.set_spacing(10)
        self.vbox_song.pack_start(self.scroll_song, expand=True)
        self.vbox_song.pack_start(self.hbox_song, expand=False)
        self.vbox_song.pack_start(self.btnbox_song, expand=False)
        #
        self.textb = gtk.TextBuffer()
        self.textv = gtk.TextView(self.textb)
        self.textv.set_size_request(300,-1)
        #
        self.scroll_note = gtk.ScrolledWindow()
        self.scroll_note.set_policy(gtk.POLICY_AUTOMATIC,
            gtk.POLICY_AUTOMATIC)
        self.scroll_note.add(self.textv)
        #
        self.btn_save = gtk.Button(stock=gtk.STOCK_SAVE)
        self.btn_save.connect('clicked', self.save_comment)
        #
        self.vbox_note = gtk.VBox()
        self.vbox_note.pack_start(self.scroll_note, expand=True)
        self.vbox_note.pack_start(self.btn_save, expand=False)
        #
        self.hbox_main = gtk.HBox()
        self.hbox_main.set_spacing(20)
        self.hbox_main.pack_start(self.vbox_song)
        self.hbox_main.pack_start(self.vbox_note)
        #
        self.win.add(self.hbox_main)
        self.win.show_all()
        #
        self.tid = gobject.timeout_add(1000, self.check_song)
    
    def initdb(self):
        q = '''
        create table songs(song text, comment text)
        '''    
        a = ()
        r = self.db.query(q, a)
        return r[0]
        
    def load_songs(self, widget):
        fname = self.fch.get_filename()
        if not fname:
            d = gtk.MessageDialog(self.win,
                gtk.DIALOG_MODAL,
                gtk.MESSAGE_ERROR,
                gtk.BUTTONS_OK,
                'Please select playlist first')
            d.run()
            d.destroy()
        else:
            content = [x.strip() for x in open(fname).readlines() if x.strip()]
            self.lstore.clear()
            for c in content:
                self.lstore.append([c])
    
    def select_song(self, tree, path, col):
        iter = self.lstore.get_iter(path)
        song = self.lstore.get_value(iter, 0)
        if song:
            #load text data
            q = 'select comment from songs where song=?'
            a = (song,)
            ret = self.db.query(q, a)
            if ret[1] == []:
                q = 'insert into songs(song, comment) values(?,?)'
                a = (song, '')
                ret = self.db.query(q, a)
                comment = u''
            else:
                comment = ret[1][0][0]
            #
            self.textb.set_text(comment)
            #
            #load the song
            if self.pos <= 0:
                pygame.mixer.music.load(song)
            
        
    def save_comment(self, widget):
        sel = self.treev.get_selection()
        model, iter, = sel.get_selected()
        if iter:
            song = model.get_value(iter, 0)
            if song:
                comment = self.textb.get_text(
                    self.textb.get_start_iter(),
                    self.textb.get_end_iter()
                    )
                q = 'update songs set comment=? where song=?'
                a = (comment, song)
                ret = self.db.query(q, a)
                if ret[0] > 0:
                    d = gtk.MessageDialog(self.win,
                        gtk.DIALOG_MODAL,
                        gtk.MESSAGE_ERROR,
                        gtk.BUTTONS_OK,
                        'Error saving comment')
                    d.run()
                    d.destroy()
        
    def play_song(self, widget):
        if widget.get_stock_id() == gtk.STOCK_MEDIA_PLAY:
            #playing
            sel = self.treev.get_selection()
            model, iter, = sel.get_selected()
            if iter:
                song = model.get_value(iter, 0)
                path = model.get_path(iter)                
                self.treev.row_activated(path, self.tvcol)
                #
                widget.set_stock_id(gtk.STOCK_MEDIA_PAUSE)
                pygame.mixer.music.play(0, self.pos)
                pygame.mixer.music.set_endevent(pygame.USEREVENT)
        else:
            #paused
            widget.set_stock_id(gtk.STOCK_MEDIA_PLAY)
            pygame.mixer.music.stop()
            self.pos = pygame.mixer.music.get_pos()

    def stop_song(self, widget):
        self.btn_play.set_stock_id(gtk.STOCK_MEDIA_PLAY)
        pygame.mixer.music.stop()
        self.pos = 0
        
    def check_song(self):
        if pygame.event.peek(pygame.USEREVENT):
            pygame.event.clear(pygame.USEREVENT)
            self.stop_song(self.btn_stop)
        else:
            #playing
            pass

        return True
            
if __name__ == '__main__':
    app = Main()
    gtk.main()

