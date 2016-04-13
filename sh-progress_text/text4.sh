#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo 
# simple 4
# iterate dir, check md5sum and display progress


DIR=/usr/bin
F_TEMP=/tmp/$$.temp
find $DIR -type f > $F_TEMP
F_COUNT=`cat $F_TEMP | wc -l`
F_RESULT=/tmp/$0.result
let P_DIV=$F_COUNT/100+1

rm -f $F_RESULT

PERCENT=0
for i in `seq 1 $F_COUNT`
do
	F_CHECK=`head -n$i $F_TEMP | tail -n1`

	let PERCENT=$i/$P_DIV
	printf "\r[%3d%%] Scanning $F_CHECK" $PERCENT
	echo -n '                                                                         '

	md5sum $F_CHECK >> $F_RESULT
	
done
printf "\r[100%%]" 
echo


rm -f $F_TEMP

less $F_RESULT 

