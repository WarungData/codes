#!/usr/bin/env python

#(c) Noprianto <noprianto.com>, GPL.

import sys
import xfce4.util as util

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('%s <desktop_entry_file>' %(sys.argv[0]))
    else:
        keys = ['Type', 'URL', 'Exec', 'Name']
        #
        desktop = sys.argv[1]
        entry = util.desktop_entry_new(desktop, keys)
        #
        for k in keys:
            s = '%s=%s' %(k, entry.get_string(k))
            print s


