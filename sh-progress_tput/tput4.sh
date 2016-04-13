#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using tput
# simple 4
# iterate dir, check md5sum and display nice progress



ROW=4
COL=20
CLEAR_CHAR="                                                                                            "
CHAR=#
STEP=5      # each $STEP incr  will add one $CHAR
let LENGTH=100/$STEP


function p_put
{
	let DROW=$ROW-1		
	let N=$1/$STEP		
	let N_COL=$COL+$N	
	let L_COL=$COL+$LENGTH+1	
	let S_COL=$COL+1

	# clear line
	tput cup $DROW $COL
	echo -n "$CLEAR_CHAR"

	# add desc and percent
	tput cup $DROW $COL
	echo -n "[$1%] $2"

	# put progress bar
	tput cup $ROW $COL
	echo -n '|'
	tput cup $ROW $L_COL
	echo -n '|'
	tput cup $ROW $S_COL
	for i in `seq 1 $N` 
	do
		echo -n $CHAR
	done
}


tput clear


DIR=/usr/bin
F_TEMP=/tmp/$$.temp
find $DIR -type f > $F_TEMP
F_COUNT=`cat $F_TEMP | wc -l`
F_RESULT=/tmp/$0.result
let P_DIV=$F_COUNT/100+1

rm -f $F_RESULT

PERCENT=0
p_put $PERCENT "Scanning $F_CHECK" 
for i in `seq 1 $F_COUNT`
do
	F_CHECK=`head -n$i $F_TEMP | tail -n1`

	let PERCENT=$i/$P_DIV
	p_put $PERCENT "Scanning $F_CHECK" 

	md5sum $F_CHECK >> $F_RESULT
	
done
p_put 100 "done."

echo

rm -f $F_TEMP

less $F_RESULT 
