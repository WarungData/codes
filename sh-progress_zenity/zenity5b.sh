#!/bin/sh

# progress bar demo
# Noprianto, 22 May 2006
# GPL
#
# simple progress bar demo using zenity
# simple 5b
# display nice progress while extracting tar archive (about 10% each)


function usage
{
	echo "usage: $0 <tarfile>"
	exit
}


test -z "$1" && usage

TAR="$1"
F_TEMP=/tmp/$$.temp
tar -tf "$TAR" > $F_TEMP
F_COUNT=`cat $F_TEMP | wc -l`
let P_DIV=$F_COUNT/100+1
let EACH=$P_DIV*10
let L_COUNT=$F_COUNT/$EACH+1
N=0

PERCENT=0
(
for i in `seq 1 $L_COUNT`
do
	let N=$N+$EACH
	tar -xf "$TAR" --no-recursion `head -n$N $F_TEMP | tail -n$EACH`

	let PERCENT=$i*10
	echo $PERCENT
	echo "# $N files extracted so far..." 

done
echo "100"
echo "# done."
) | zenity --progress --text="Initializing..." --auto-close 

rm -f $F_TEMP
