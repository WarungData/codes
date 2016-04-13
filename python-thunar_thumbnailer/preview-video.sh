#!/bin/sh

#(c) Noprianto, GPL.
#
#helper script
#thunar thumbnailer
#video files
#using mplayer

ifile="$1"
ofile="$2"
temp="/tmp/00000001.png"

cd /tmp
mplayer -vo png -frames 1 -nosound "$ifile" 
mv "$temp" "$ofile"

