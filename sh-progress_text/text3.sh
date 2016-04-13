#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo
# simple 3


PERCENT=0
printf "\r$PERCENT percent complete" 
for i in `seq 1 10000`
do
	let PERCENT=$i/100
	printf "\r$PERCENT percent complete" 
done

echo

