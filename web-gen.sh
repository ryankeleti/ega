#!/usr/bin/env sh

rm -rf web-build/
make web
mkdir web-build/
cd web-build/
mkdir WEB/
cp ../ega.tex ../ega-bib.bib ../tags WEB/
virtualenv venv/
source venv/bin/activate
pip install unidecode
pip install jinja2
git clone https://github.com/gerby-project/plastex.git
#git clone https://github.com/ryankeleti/plastex.git
cd plastex/
git fetch origin pull/58/head:gerby2
git checkout gerby2
pip install .
cd ../WEB/
plastex --renderer=Gerby ega.tex
cd ega/
python ../../../scripts/tohtml.py .

