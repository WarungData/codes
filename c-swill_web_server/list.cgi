#!/bin/sh

ROOT=$1

[ -z "$ROOT" ] && exit 1

echo "<html>"
echo "<head></head>"
echo "<body>"
echo "<table border='1'>"
for i in `ls -1 $ROOT/*`
do
	f=$(basename $i)
	s=$(ls -l $i | awk '{print $5}')
	l="<a href='$f'>$f</a>"
	echo "<tr><td>$l</td><td align='right'>$s</td></tr>"
	
done
echo "</table>"
echo "</body>"
echo "</html>"
