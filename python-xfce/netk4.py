#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, 2009, GPL.

import xfce4.netk as netk

if __name__ == '__main__':
    screen = netk.screen_get_default()
    windows = screen.get_windows()
    for w in windows:
        app = w.get_application()
        s = '[XID: %d] %s' %(app.get_xid(), app.get_name())
        print s
