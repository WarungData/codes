#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using zenity
# simple 1b


(
sleep 1
echo 10
echo "# 10 percent complete" 

sleep 3
echo 85
echo "# 85 percent complete" 

sleep 3
echo 100
echo "# done." 

) | zenity --progress --text="Initializing..." --auto-close

