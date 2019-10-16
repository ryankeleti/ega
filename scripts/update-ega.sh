#!/usr/bin/env sh

# basic template I use for serving EGA PDFs.
# change paths as needs, using absolute paths.
# then crontab -e, and add the entry
# 0 * * * * /path/to/script/update-ega.sh
# make sure to chmod +x the script!

set -x

CDIR=/path/to/where/script/is
EGA=$CDIR/ega
SURL=/path/to/server/files/ega

if [ ! -d "$EGA" ]; then
  git clone https://github.com/ryankeleti/ega.git "$EGA"
fi

cd "$EGA"
git fetch
if [ $(git rev-parse HEAD) != $(git rev-parse @{u}) ]; then
  git pull
  make auto
  mv "$EGA"/pdfs/book-auto.pdf "$SURL"/book-auto.pdf
  mv "$EGA"/pdfs/what-auto.pdf "$SURL"/what-auto.pdf
  mv "$EGA"/pdfs/intro-auto.pdf "$SURL"/intro-auto.pdf
  mv "$EGA"/pdfs/ega0-auto.pdf "$SURL"/ega0-auto.pdf
  mv "$EGA"/pdfs/ega1-auto.pdf "$SURL"/ega1-auto.pdf
  mv "$EGA"/pdfs/ega2-auto.pdf "$SURL"/ega2-auto.pdf
  mv "$EGA"/pdfs/ega3-auto.pdf "$SURL"/ega3-auto.pdf
  mv "$EGA"/pdfs/ega4-auto.pdf "$SURL"/ega4-auto.pdf
  mv "$EGA"/pdfs/ref-auto.pdf "$SURL"/ref-auto.pdf
fi

cat <<KITTY > "$SURL"/index.html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ega files</title>
</head>
<body>
<p>last updated :: `date`.</p>
<p>git hash     :: `cd $EGA && git rev-parse HEAD`.</p>
<p>source files :: <a href="https://github.com/ryankeleti/ega">github.com/ryankeleti/ega</a>.</p>
<p><a href="book-auto.pdf">Full document</a>.</p>
<p><a href="what-auto.pdf">What this is</a>.</p>
<p><a href="intro-auto.pdf">Introduction</a>.</p>
<p><a href="ega0-auto.pdf">EGA 0</a>.</p>
<p><a href="ega1-auto.pdf">EGA I</a>.</p>
<p><a href="ega2-auto.pdf">EGA II</a>.</p>
<p><a href="ega3-auto.pdf">EGA III</a>.</p>
<p><a href="ega4-auto.pdf">EGA IV</a>.</p>
<p><a href="ref-auto.pdf">References</a>.</p>
<p><a href="yoursite.com">return to site home</a>.</p>
</body>
</html>
KITTY

