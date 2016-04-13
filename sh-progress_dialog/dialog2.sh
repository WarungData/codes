#!/bin/sh

# progress bar demo
# Noprianto, 17 April 2006
# GPL
#
# simple progress bar demo using dialog
# simple 2


PERCENT=0
(
while [ 1 ]
do
	sleep 1
	let PERCENT=$PERCENT+10
	echo "XXX"
	echo $PERCENT
	echo "$PERCENT percent complete" 
	echo "XXX"
	test $PERCENT -eq 100 && exit
done
) | dialog --gauge "Initializing..." 8 40 0

