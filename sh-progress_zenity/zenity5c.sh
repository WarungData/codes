#!/bin/sh

# progress bar demo
# Noprianto, 22 May 2006
# GPL
#
# simple progress bar demo using zenity
# simple 5c
# display nice progress while extracting tar archive (about 10% each)
# fix handling information about count of extracted files
# - revision 1 23 May 2006


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

if [ $F_COUNT -lt 20 ] 
then
	let L_COUNT=1
else
	let L_COUNT=10
fi

let P_MOD=100/$L_COUNT
let EACH=$F_COUNT/10+1
N=0

PERCENT=0
(
for i in `seq 1 $L_COUNT`
do
	
	if [ $i -eq $L_COUNT ]
	then
		let N=$F_COUNT
	else
		let N=$N+$EACH
	fi
	
	tar -xf "$TAR" --no-recursion `head -n$N $F_TEMP | tail -n$EACH`
	
	let PERCENT=$i*$P_MOD
	echo $PERCENT
	
	echo "# $N files extracted so far..." 
	


done
echo "100"
echo "# done, $F_COUNT files extracted."
) | zenity --progress --text="Initializing..."  

rm -f $F_TEMP
