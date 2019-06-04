#!/usr/bin/env sh

mkdir ega-web-build/
cd ega-web-build
virtualenv venv/
source venv/bin/activate
git clone https://github.com/ryankeleti/plastex.git
cd plastex/
pip install .
cd ../
git clone https://github.com/live-clones/pybtex.git
wget https://bitbucket.org/pybtex-devs/pybtex/issues/attachments/110/pybtex-devs/pybtex/1514284299.07/110/no-protected-in-math-mode.patch
cd pybtex/
git apply ../no-protected-in-math-mode.path
pip install .
cd ../
git clone https://github.com/ryankeleti/en.ega.git
mkdir WEB/
cd en.ega/
make web
make tags
cp ega-web.tex tags ega-bib.bib ../WEB/
cd ../WEB/
plastex --renderer=HTML5 ega-web.tex
#git clone https://github.com/sonoisa/XyJax.git
#sed -i -e 's@\[MathJax\]@/static/XyJax@' XyJax/extensions/TeX/xypic.js

