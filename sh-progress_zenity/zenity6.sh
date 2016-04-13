#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using zenity
# simple 6
# display nice progress while extracting tar.gz archive


function usage
{
	echo "usage: $0 <targzfile>"
	exit
}


test -z "$1" && usage

TAR="$1"
F_TEMP=/tmp/$$.temp
tar -tzf "$TAR" > $F_TEMP
F_COUNT=`cat $F_TEMP | wc -l`
let P_DIV=$F_COUNT/100+1

PERCENT=0
(
for i in `seq 1 $F_COUNT`
do
	F_CHECK=`head -n$i $F_TEMP | tail -n1`

	let PERCENT=$i/$P_DIV
	echo $PERCENT
	echo "# Extracting $F_CHECK" 

	tar -zxf "$TAR" --no-recursion $F_CHECK
	
done
echo "100"
echo "# done."
) | zenity --progress --text="Initializing..." 

rm -f $F_TEMP
