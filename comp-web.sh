#!/bin/sh

export PYTHONPATH=.
export TEXINPUTS=.:.::
export XHTMLTEMPLATES=.
mkdir WEB/
cd WEB/
python2 ../gen-web.py > web.tex
python2 ../tagger.py > tags
#latex2html web.tex
#plastex --renderer=Gerby web.tex
plastex web.tex

