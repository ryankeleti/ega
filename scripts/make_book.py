from functions import *

def print_list_contrib(path):
  filename = path + 'CONTRIBUTORS.md'
  CONTRIBUTORS = open(filename, 'r')
  first = 1
  for line in CONTRIBUTORS:
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
  CONTRIBUTORS.close()
  print contributors

path = get_path() 
with open(path + "preamble.tex", 'r') as preamble:
  for line in preamble:
    if line.find("%") == 0:
      continue
    if line.find("externaldocument") >= 0:
      continue
    if line.find("xr-hyper") >= 0:
      line = line.replace("xr-hyper", "CJKutf8")
    if line.find("\\documentclass") == 0:
      line = line.replace("amsart", "amsbook")
    print line,
print "\\begin{document}"
print "\\begin{titlepage}"
print "\\pagestyle{empty}"
print "\\setcounter{page}{1}"
print "\\centerline{\\LARGE\\bfseries \\'El\\'ements de g\\'eom\\'etrie alg\\'ebrique}"
print "\\vskip1in"
print "\\noindent"
print "\\centerline{A.~Grothendieck and J.~Dieudonn\\'e}"
print "\\centerline{Publications math\\'ematiques de l'I.H.\\'E.S}"
print "\\vskip1in"
print "\\noindent"
print "\\centerline{\\bfseries Contributors}"
print "\\centerline{"
print_list_contrib(path)
print "}"
print ""
print "\\end{titlepage}"

for name in list_text_files(path):
  with open(path + name + ".tex", 'r') as f:
    verbatim = 0
    for line in f:
      verbatim += beginning_of_verbatim(line)
      if verbatim:
        if end_of_verbatim(line):
          verbatim = 0
        if name != 'intro':
          print line,
        continue
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
#    if is_label(line):
#      line = line.replace("\\label{", "\\label{" + name + "-")
#    if contains_ref(line):
#      line = replace_refs(line, name)
      print line,

print "\\bibliography{ega-bib}"
print "\\bibliographystyle{amsalpha}"
print "\\end{document}"

