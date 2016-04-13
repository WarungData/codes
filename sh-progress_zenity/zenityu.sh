#!/bin/sh

# progress bar demo
# Noprianto, 21 April 2006
# GPL
#
# simple progress bar demo using zenity
# simple u
# uncertainty

(
	find /usr

) | zenity --progress --text="Please wait..." --pulsate 

