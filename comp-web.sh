#!/bin/sh

make cleanweb
export PYTHONPATH=.
export TEXINPUTS=.:.::
export XHTMLTEMPLATES=.
mkdir -p ../ega/
python2 gen-web.py > ../ega/ega.tex
python tagger.py > ../ega/tags
#latex2html ega.tex
cd ../ega/
#plastex --renderer=Gerby ega.tex
plastex --renderer=XHTML --theme=default ega.tex

