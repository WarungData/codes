#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo
# simple u

TEMP=0

while [ 1 ]
do
	echo -n '#'

	let TEMP=$TEMP+1
	test $TEMP -eq 1000 && break
done


