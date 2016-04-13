#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo
# simple 3b


PERCENT=0
CHAR='-'
for i in `seq 1 10000`
do
	let PERCENT=$i/100

	case $CHAR in
	'-'	)	CHAR='\'
		;;
	'\'	)	CHAR='|'
		;;
	'|'	)	CHAR='/'
		;;
	'/'	)	CHAR='-'
		;;
	esac
	
	printf "\r$CHAR" 
	
done

printf "\rdone." 
echo

