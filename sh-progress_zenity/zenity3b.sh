#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using zenity
# simple 3b


PERCENT=0
(
for i in `seq 1 10000`
do
	let PERCENT=$i/100
	echo $PERCENT
	echo "# $PERCENT percent complete" 
done
) | zenity --progress --text="Initializing..." --auto-close
