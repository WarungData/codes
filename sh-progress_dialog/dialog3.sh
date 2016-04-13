#!/bin/sh

# progress bar demo
# Noprianto, 17 April 2006
# GPL
#
# simple progress bar demo using dialog
# simple 3


PERCENT=0
(
for i in `seq 1 10000`
do
	let PERCENT=$i/100
	echo "XXX"
	echo $PERCENT
	echo "$PERCENT percent complete" 
	echo "XXX"
done
) | dialog --gauge "Initializing..." 8 40 0

