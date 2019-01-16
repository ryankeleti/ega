#!/bin/sh

mkdir WEB/
cd WEB/
python2 ../gen-web.py > web.tex
python2 ../tagger.py > tags
latex2html web.tex

