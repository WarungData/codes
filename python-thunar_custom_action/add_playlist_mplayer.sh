#!/bin/sh

#add Mplayer playlist
#play the playlist
#
#thunar custom action
#for video and audio files
#
#(c) Noprianto, GPL.

#creating the playlist
PLIST=/tmp/playlist.$USER
rm -f $PLIST
for i in "$@"
do
    echo "$i" >> $PLIST
done

#call gmplayer
gmplayer -playlist $PLIST
