#!/bin/sh

# progress bar demo
# Noprianto, 17 April 2006
# GPL
#
# simple progress bar demo using dialog
# simple 4
# iterate dir, check md5sum and display nice progress


DIR=/usr/bin
F_TEMP=/tmp/$$.temp
find $DIR -type f > $F_TEMP
F_COUNT=`cat $F_TEMP | wc -l`
F_RESULT=/tmp/$0.result
let P_DIV=$F_COUNT/100+1

rm -f $F_RESULT

PERCENT=0
(
for i in `seq 1 $F_COUNT`
do
	F_CHECK=`head -n$i $F_TEMP | tail -n1`

	let PERCENT=$i/$P_DIV
	echo "XXX"
	echo $PERCENT
	echo "Scanning $F_CHECK" 
	echo "XXX"

	md5sum $F_CHECK >> $F_RESULT
	
done
echo "XXX"
echo "100"
echo "done."
echo "XXX"
) | dialog --gauge "Initializing..." 8 70 0

rm -f $F_TEMP

dialog --textbox $F_RESULT 20 70
