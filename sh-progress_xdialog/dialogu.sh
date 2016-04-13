#!/bin/sh

# progress bar demo
# Noprianto, 17 April 2006
# GPL
#
# simple progress bar demo using dialog
# simple u
# uncertainty

TEMP=0

PERCENT=4
DX=2
(
while [ 1 ]
do
	let TEMP=TEMP+1
	test $TEMP -eq 8888 && break


	if [ $PERCENT -eq 98 ] || [ $PERCENT -eq 2 ] 
	then
		let DX=$DX*-1
	fi
	
	
	let PERCENT=$PERCENT+$DX

	echo "XXX"
	echo $PERCENT
	echo "Please wait..." 
	echo "XXX"
done
) | dialog --gauge "Initializing..." 8 40 0

