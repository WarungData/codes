#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using zenity
# simple 1


(
sleep 1
echo 10
echo "# 10 percent complete" 

sleep 3
echo 50
echo "# 50 percent complete" 

sleep 3
echo 100
echo "# done." 

) | zenity --progress --text="Initializing..." 

