#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using tput
# simple 2

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

PERCENT=0
p_put $PERCENT " complete"	
while [ 1 ]
do
	sleep 1
	let PERCENT=$PERCENT+10
	p_put $PERCENT " complete"	
	test $PERCENT -eq 100 && break
done

echo
