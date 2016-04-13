#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.

import xfce4.netk as netk

if __name__ == '__main__':
    screen = netk.screen_get_default()
    workspaces = screen.get_workspaces()
    for w in workspaces:
        s = 'workspace %d, height: %d, width: %d' %(
            w.get_number(), w.get_height(), w.get_width())
        print s
