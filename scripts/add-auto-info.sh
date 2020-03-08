#!/usr/bin/env sh

#
# script to add build information to the TeX files before compiling them to PDFs.
# information added:
#  - time built
#  - git commit hash (with link)
#  - source link
#

if [ $# != 1 ]; then
  echo "$0: must take one argument, the file to add to be modified."
  return
fi

DATE="$(date -u +"%F %H:%M %Z")"
COMMIT="\\\href{https://github.com/ryankeleti/ega/commit/$(git rev-parse HEAD)}{$(git rev-parse --short HEAD)}"
SOURCE="\\\href{https://github.com/ryankeleti/ega}{github.com/ryankeleti/ega}"
TABLE="\\\begin{center}\\\texttt{\\\begin{tabular}{lcl}autobuild \& :: \& $DATE\\\\\\\\ git commit \& :: \& $COMMIT\\\\\\\\ source \& :: \& $SOURCE\\\end{tabular}}\\\end{center}"

sed -i "s|\\\end{titlepage}|\\\vskip0.5in\\\noindent $TABLE \\\end{titlepage}|" "$1"
sed -i "s|\\\maketitle|\\\maketitle\\\noindent $TABLE\\\vskip0.25in|" "$1"


