#!/bin/bash
read -r -p "What file?" name
echo "$name"
git add $name
git status
read -r -p "Continue?(Y/N)" continue_yn
if [ "continue_yn"="Y"]; then
	read -r -p "Type your commit message:" commit_msg
elif [ "continue_yn"="N"]; then
	exit 1
fi
git commit -$commit_msg
git status
