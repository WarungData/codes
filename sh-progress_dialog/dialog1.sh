#!/bin/sh

# progress bar demo
# Noprianto, 17 April 2006
# GPL
#
# simple progress bar demo using dialog
# simple 1


(
sleep 1
echo "XXX"
echo 10
echo "10 percent complete" 
echo "XXX"

sleep 3
echo "XXX"
echo 50
echo "50 percent complete" 
echo "XXX"

sleep 3
echo "XXX"
echo 100
echo "done." 
echo "XXX"

) | dialog --gauge "Initializing..." 8 40 0

