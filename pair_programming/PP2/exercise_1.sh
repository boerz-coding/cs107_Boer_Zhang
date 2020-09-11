#!/bin/bash
read -r -p "Which file to add?" name
echo "$name"
git add $name
git status
read -r -p "Continue?(Y/N)" continue_yn
if [ "continue_yn"="Y"]; then
	read -r -p "Type your commit message:" commit_msg
elif [ "continue_yn"="N"]; then
	exit 1
fi
git commit -m $commit_msg
git status
read -r -p "Continue?(Y/N)" continue_yn
if ["continue_yn"="Y"]; then
	git push
fi


