#!/usr/bin/env sh
# modified from https://github.com/gerby-project/hello-world/.travis.yml
#      and from https://github.com/gerby-project/gerby-website/.travis.yml

set -x

BASE=$HOME/ega
EGA_DIR="$BASE"
FNAME=ega
EGA_SRC=https://github.com/ryankeleti/ega.git
PLASTEX_SRC=https://github.com/ryankeleti/plastex.git
GERBY_WEBSITE_SRC=https://github.com/ryankeleti/gerby-website.git
BONSAI_SRC=https://github.com/ryankeleti/jquery-bonsai.git
PYBTEX_SRC=https://github.com/ryankeleti/pybtex.git
XYJAX_SRC=https://github.com/ryankeleti/XyJax.git

# 0) make sure dvipng can be found.
#sudo apt-get update
#sudo apt install dvipng

if [ -z "$1" ]; then
  echo "\$BASE defaulting to $BASE"
else
  BASE=$(readlink -f "$1")
fi

cd "$BASE" || return

rm -rf tags "$FNAME" "$FNAME".* "$BASE"/plastex "$BASE"/gerby-website "$BASE"/env
cp "$BASE"/scripts/configuration.py "$BASE"/configuration.py
python3 "$BASE"/scripts/make_web.py "$BASE"

#
# install.
#

python3 -m venv "$BASE"/env
source "$BASE"/env/bin/activate

#git clone "$EGA_SRC" "$EGA_DIR"
pip install unidecode

# 1) install plasTeX.
git clone "$PLASTEX_SRC"
cd "$BASE"/plastex/ || return
# use the Gerby branch of plasTeX.
git checkout gerby
# actual install.
pip install .
cd "$BASE" || return

# 2) install Gerby.
git clone "$GERBY_WEBSITE_SRC"
cd "$BASE"/gerby-website/gerby/static/ || return
# import jQuery Bonsai.
git clone "$BONSAI_SRC"
cp jquery-bonsai/jquery.bonsai.css css/
# import pybtex.
git clone "$PYBTEX_SRC"
#wget https://bitbucket.org/pybtex-devs/pybtex/issues/attachments/110/pybtex-devs/pybtex/1514284299.07/110/no-protected-in-math-mode.patch
cd pybtex || return
git apply ./no-protected-in-math-mode.patch
pip install .
cd .. || return
# import XyJax.
git clone "$XYJAX_SRC"
sed -i -e 's@\[MathJax\]@/static/XyJax@' XyJax/extensions/TeX/xypic.js

# actual install.
cd "$BASE"/gerby-website/ || return
# we use -e because we want to change the source files.
pip install -e .
cd "$BASE" || return

# 3) setup configuration.
mv "$EGA_DIR"/configuration.py "$BASE"/gerby-website/gerby/configuration.py

# 4) setup soft links for plasTeX output.
cd "$BASE"/gerby-website/gerby/tools/ || return
ln -s ../../../"$FNAME"      "$FNAME"
ln -s ../../../"$FNAME".paux "$FNAME".paux
ln -s ../../../tags          tags

# 5) setup soft links for database.
cd "$BASE"/gerby-website/ || return
ln -s gerby/tools/"$FNAME".sqlite   "$FNAME".sqlite
cd "$BASE" || return

