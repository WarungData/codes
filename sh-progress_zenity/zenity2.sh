#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using zenity
# simple 2


PERCENT=0
(
while [ 1 ]
do
	sleep 1
	let PERCENT=$PERCENT+10
	echo $PERCENT
	echo "# $PERCENT percent complete" 
done
) | zenity --progress --text="Initializing..." --auto-close 

