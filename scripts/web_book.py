from functions import *

def print_preamble(path):
  preamble.close()
  return

path = get_path()
  
with open(path + "preamble.tex", 'r') as preamble:
  next(preamble)
  next(preamble)
  next(preamble)
  next(preamble)
  next(preamble)
  print "\\documentclass{book}"
  print "\\usepackage{amsmath}"
  for line in preamble:
    if line.find("%") == 0:
      continue
    if line.find("externaldocument") >= 0:
      continue
    if line.find("multicol")>= 0:
      continue
    if line.find("xr-hyper") >= 0:
      continue
    if line.find("mathdesign") >= 0:
      continue
    print line,

print "\\begin{document}"
print "\\begin{titlepage}"
print "\\pagestyle{empty}"
print "\\setcounter{page}{1}"
print "\\centerline{\\LARGE\\bfseries \\'El\\'ements de g\\'eom\\'etrie alg\\'ebrique}"
print "\\vskip1in"
print "\\noindent"
print "\\end{titlepage}"

#parts = get_parts(path)
for name in list_text_files(path):
#  if name in parts:
#    print "\\part{" + parts[name][0] + "}"
#    print "\\label{" + parts[name][1] + "}"
  with open(path + name + ".tex", 'r') as f:
    for line in f:
#      if name != 'intro':
#        print line,
#        continue
      if line.find("\\input{preamble}") == 0:
        continue
      if line.find("\\begin{document}") == 0:
        continue
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
#      if is_label(line):
#        line = line.replace("\\label{", "\\label{" + name + "-")
#      if contains_ref(line):
#        line = replace_refs(line, name)
      print line,

print "\\bibliography{ega-bib}"
print "\\bibliographystyle{amsalpha}"
print "\\end{document}"

