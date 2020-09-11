#!/bin/bash
read -r -p "Which file to add?" name
echo "$name"
git add $name
git status
read -r -p "Continue?(Y/N)" continue_yn
if [ "$continue_yn" = "Y" ]; then
	echo Yes
	read -r -p "Type your commit message:" commit_msg
	echo "$commit_msg"
else
	exit 1
fi
git commit -m $commit_msg
git status
read -r -p "Continue?(Y/N)" continue_yn
if [ "$continue_yn"="Y" ]; then
	git push
fi


