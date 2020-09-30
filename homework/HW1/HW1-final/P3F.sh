#!/bin/bash
for name in $( ls )
do
        if [ -f "$name" ]; then
                echo "$name $( cat $name|wc -l )"
        fi
done
