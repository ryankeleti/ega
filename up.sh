#!/bin/sh

git add --all
echo 'enter commit msg --- '
read msg
git commit -m $msg
git push -u origin master


