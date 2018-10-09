#!/bin/sh

unset msg
git add --all
echo -n "enter commit msg --- "
read msg
git commit -m $msg
git push -u origin master


