# see README.md/COPYING.md.
import re

# get location of repo.
def get_path():
  from sys import argv
  if not len(argv) == 2:
    print("\nThis script needs exactly one argument,")
    print("namely the path to the EGA directory\n")
    raise Exception('Wrong arguments')
  return argv[1].rstrip("/") + "/"

# list the stems of the TeX files in the project in the correct order.
def list_text_files(path):
  with open(path + "makefile", 'r') as f:
    for line in f:
      if line.find("FILES = ") == 0:
        break
    listf = ""
    while line.find("\\") >= 0:
      line = line.rstrip()
      line = line.rstrip("\\")
      listf += " " + line
      line = f.next()
  listf += " " + line
  listf = listf.replace("FILES = ", "")
  return listf.split()

path = get_path() 
with open(path + "preamble.tex", 'r') as preamble:
  for line in preamble:
    if line.find("%") == 0:
      continue
    if line.find("externaldocument") >= 0:
      continue
    if line.find("xr-hyper") >= 0:
      line = line.replace("xr-hyper", "CJKutf8")
    if line.find("\\documentclass[oneside]") == 0:
      line = line.replace("[oneside]{amsart}", "[openany,oneside]{amsbook}")
    if line.find("\\documentclass") == 0:
      line = line.replace("{amsart}", "[openany,oneside]{amsbook}")
    print(line, end='')
print("\\newcommand{\\ZeroRoman}[1]{\\ifcase\\value{#1}\\relax 0\\else\\Roman{#1}\\fi}")
print("\\renewcommand{\\thechapter}{\\ZeroRoman{chapter}}")
print("\\begin{document}")
print("\\begin{titlepage}")
print("\\pagestyle{empty}")
print("\\setcounter{page}{1}")
print("\\centerline{\\LARGE\\bfseries \\'El\\'ements de g\\'eom\\'etrie alg\\'ebrique}")
print("\\vskip1in")
print("\\noindent")
print("\\centerline{A.~Grothendieck and J.~Dieudonn\\'e}")
print("\\centerline{Publications math\\'ematiques de l'I.H.\\'E.S}")
print("\\vskip1in")
print("\\noindent")
print("\\centerline{\\bfseries Contributors}")
print("\\centerline{")
with open(path + "CONTRIBUTORS", 'r') as f:
  first = 1
  for line in f:
    if line.find("%") == 0:
      continue
    if len(line.rstrip()) == 0:
      continue
    contributor = line.rstrip()
    contributor = contributor.replace("(", "(\\begin{CJK}{UTF8}{min}")
    contributor = contributor.replace(")", "\\end{CJK})")
    if first:
      contributors = contributor
      first = 0
      continue
    contributors += ", " + contributor
print(contributors)
print("}")
print("\\end{titlepage}")
print("\\setcounter{tocdepth}{2}")
print("\\tableofcontents{}")

for name in list_text_files(path):
  with open(path + name + ".tex", 'r') as f:
    for line in f:
      if line.find("\\input{preamble}") == 0:
        continue
      if line.find("\\begin{document}") == 0:
        continue
      if line.find("\\title{What this is}") == 0:
        line = line.replace("\\title{What this is}", "\\chapter*{What this is}")
      if line.find("\\title{Introduction}") == 0:
        line = line.replace("\\title{Introduction}", "\\chapter*{Introduction}")
      if line.find("\\title{Preliminaries}") == 0:
        line = line.replace("\\title{Preliminaries}", "\\setcounter{chapter}{-1}\\chapter{Preliminaries}")
      if line.find("\\title{") == 0:
        line = line.replace("\\title{", "\\chapter{")
      if line.find("\\maketitle") == 0:
        continue
      if line.find("\\tableofcontents") == 0:
        continue
      if line.find("\\bibliography") == 0:
        continue
      if line.find("\\end{document}") == 0:
        continue
      print(line, end='')

print("\\bibliography{the}")
print("\\bibliographystyle{amsalpha}")
print("\\end{document}")

