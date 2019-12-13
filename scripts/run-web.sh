#!/usr/bin/env sh

set -x

BASE=$HOME/ega
EGA_DIR="$BASE"

if [ -z "$1" ]; then
  echo "\$BASE defaulting to $BASE"
else
  BASE=$(readlink -f "$1")
fi

cd "$EGA_DIR" || return
./scripts/update-web.sh

#
# run.
#

# run Flask.
# need to set up a WSGI.
cd "$BASE"/gerby-website/ || return
export FLASK_APP=gerby
python3 -m flask run &

# testing the setup.
#sleep 1
#wget http://127.0.0.1:5000/tag/0001
#cat 0001

