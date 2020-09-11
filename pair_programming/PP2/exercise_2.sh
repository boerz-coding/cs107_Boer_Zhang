#!/bin/bash
#echo "$( ls )"
for name in $( ls )
do
	#echo "file is $name"
	if [ -x "$name" ]; then
		echo "$name"
	fi
done
