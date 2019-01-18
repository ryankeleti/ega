#!/bin/sh

export PYTHONPATH=.
export TEXINPUTS=.:.::
export XHTMLTEMPLATES=.
mkdir -p ../ega/
python2 ./gen-web.py > ../ega/web.tex
#python2 ./tagger.py > ../ega/tags
#latex2html web.tex
#plastex --renderer=Gerby web.tex
cd ../ega/
plastex --renderer=XHTML web.tex

