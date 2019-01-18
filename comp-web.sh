#!/bin/sh

export PYTHONPATH=.
export TEXINPUTS=.:.::
export XHTMLTEMPLATES=.
mkdir -p ../ega/
python2 ./gen-web.py > ../ega/ega.tex
#python2 ./tagger.py > ../ega/tags
#latex2html ega.tex
#plastex --renderer=Gerby ega.tex
cd ../ega/
plastex --renderer=XHTML ega.tex

