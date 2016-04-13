#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo 
# simple 2


PERCENT=0
printf "\r$PERCENT percent complete" 
while [ 1 ]
do
	sleep 1
	let PERCENT=$PERCENT+10
	printf "\r$PERCENT percent complete" 
	test $PERCENT -eq 100 && break
done

echo
