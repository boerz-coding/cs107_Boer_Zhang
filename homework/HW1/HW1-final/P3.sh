#!/bin/bash
grep '[0-9]' apollo13.txt|wc -l
grep --help|grep -- --count
ls *.py|cat|wc -l
find ! -perm -006|wc -l
find -maxdepth 1 ! -perm -006|wc -l
