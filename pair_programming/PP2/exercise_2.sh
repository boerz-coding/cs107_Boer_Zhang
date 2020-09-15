#!/bin/bash
#sharer:Blake
#coder: Zhufeng
#Listener: Boer and Little
#echo "$( ls )"
for name in $( ls )
do
	#echo "file is $name"
	if [ -x "$name" ]; then
		echo "$name"
	fi
done
