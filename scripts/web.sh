#!/bin/bash
# modified from https://github.com/gerby-project/hello-world/.travis.yml
#      and from https://github.com/gerby-project/gerby-website/.travis.yml

#
# set base directory here (where everything takes place).
#
BASE=$HOME/ega
#
# set where ega directory is (by default, ega directory is base).
#
EGA_DIR="$BASE"
FNAME=ega
EGA_SRC=https://github.com/ryankeleti/ega.git
PLASTEX_SRC=https://github.com/ryankeleti/plastex.git
GERBY_WEBSITE_SRC=https://github.com/ryankeleti/gerby-website.git
BONSAI_SRC=https://github.com/ryankeleti/jquery-bonsai.git
PYBTEX_SRC=https://github.com/ryankeleti/pybtex.git
XYJAX_SRC=https://github.com/ryankeleti/XyJax.git
PIPLOC="$BASE"/env/bin

clean_web() {
  cd "$BASE" || return
  rm -rf tags "$FNAME" "$FNAME".* "$BASE"/plastex "$BASE"/gerby-website "$BASE"/env
  cp "$BASE"/scripts/configuration.py "$BASE"/configuration.py
  python3 "$BASE"/scripts/make_web.py "$BASE"
}

setup_web() {
  command -v dvipng >/dev/null 2>&1 || { echo >&2 "need to install dvipng"; exit 1; }

  echo "*** setting up python virtual environment ***"
  python3 -m venv "$BASE"/env
  source "$BASE"/env/bin/activate

  echo "*** installing unidecode ***"
  #git clone "$EGA_SRC" "$EGA_DIR"
  pip install unidecode

  echo "*** installing plastex ***"
  # 1) install plasTeX.
  git clone "$PLASTEX_SRC"
  cd "$BASE"/plastex/ || return
  # use the Gerby branch of plasTeX.
  git checkout gerby
  # actual install.
  pip install .
  cd "$BASE" || return

  echo "*** downloading gerby-website ***"
  # 2) install Gerby.
  git clone "$GERBY_WEBSITE_SRC"

  echo "*** downloading jquery-bonsai ***"
  # import jQuery Bonsai.
  cd "$BASE"/gerby-website/gerby/static/ || return
  git clone "$BONSAI_SRC"
  cp jquery-bonsai/jquery.bonsai.css css/

  echo "*** downloading/installing pybtex ***"
  # import pybtex.
  git clone "$PYBTEX_SRC"
  cd pybtex || return
  git apply ./no-protected-in-math-mode.patch
  pip install .

  echo "*** downloading xyjax ***"
  # import XyJax.
  cd .. || return
  git clone "$XYJAX_SRC"
  sed -i -e 's@\[MathJax\]@/static/XyJax@' XyJax/extensions/TeX/xypic.js

  echo "*** installing gerby-website ***"
  # actual install.
  cd "$BASE"/gerby-website/ || return
  # we use -e because we want to change the source files.
  pip install -e .
  cd "$BASE" || return

  echo "*** moving configuration.py ***"
  # 3) setup configuration.
  mv "$EGA_DIR"/scripts/configuration.py "$BASE"/gerby-website/gerby/configuration.py

  echo "*** linking files for plastex ***"
  # 4) setup soft links for plasTeX output.
  cd "$BASE"/gerby-website/gerby/tools/ || return
  ln -s ../../../"$FNAME"      "$FNAME"
  ln -s ../../../"$FNAME".paux "$FNAME".paux
  ln -s ../../../tags          tags

  echo "*** linking sqlite database ***"
  # 5) setup soft links for database.
  cd "$BASE"/gerby-website/ || return
  ln -s gerby/tools/"$FNAME".sqlite   "$FNAME".sqlite
  cd "$BASE" || return
}

update_web() {
  cd "$BASE" || return
  #git fetch
  #if [ "$(git rev-parse HEAD)" != "$(git rev-parse @{u})" ]; then
  #  git pull
  rm -rf tags "$FNAME"
  python3 "$EGA_DIR"/scripts/make_web.py "$EGA_DIR"

  # 1) update tags file with new tags.
  python3 "$EGA_DIR"/scripts/tagger.py "$FNAME".tex > tags

  # 2) convert to HTML: output goes to $FNAME/
  "$PIPLOC"/plastex --renderer=Gerby ./"$FNAME".tex

  # 3) import CONTRIBUTORS.
  if [ ! -d "$BASE"/gerby-website/gerby/tex ]; then
    mkdir -p "$BASE"/gerby-website/gerby/tex
  fi
  curl https://raw.githubusercontent.com/ryankeleti/ega/master/CONTRIBUTORS -o "$BASE"/gerby-website/gerby/tex/CONTRIBUTORS

  # 4) import plasTeX output into database.
  cd "$BASE"/gerby-website/gerby/tools/ || return
  python3 update.py
  #fi
}

run_web() {
  update_web
  cd "$BASE" || return

  # run Flask.
  # need to set up a WSGI.
  cd "$BASE"/gerby-website/ || return
  export FLASK_APP=gerby
  python3 -m flask run &
}

if [ "$#" != 1 ]; then
  echo "$0 must take one arg"
  exit 1
fi

if [ "$#" == 1 ]; then
  if [ "$1" == "setup" ]; then
    setup_web
  elif [ "$1" == "update" ]; then
    update_web
  elif [ "$1" == "run" ]; then
    run_web
  elif [ "$1" == "clean" ]; then
    clean_web
  else echo "$0 [ setup update run clean ]"
  fi
fi

