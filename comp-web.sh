#!/bin/sh

export PYTHONPATH=.
export TEXINPUTS=.:.::
export XHTMLTEMPLATES=.
mkdir -p ../ega/
python2 gen-web.py > ../ega/ega.tex
python tagger.py > ../ega/tags
#latex2html ega.tex
cd ../ega/
plastex --renderer=Gerby ega.tex
#plastex --renderer=XHTML ega.tex

