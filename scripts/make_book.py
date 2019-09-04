# see README.md/COPYING.md.

# get location of repo.
def get_path():
  from sys import argv
  if not len(argv) == 2:
    print("\nThis script needs one argument, the path to the EGA directory.\n")
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
with open(path + "book.tex", 'w') as book:
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
      book.write(line)
  book.write("\\newcommand{\\ZeroRoman}[1]{\\ifcase\\value{#1}\\relax 0\\else\\Roman{#1}\\fi}\n")
  book.write("\\renewcommand{\\thechapter}{\\ZeroRoman{chapter}}\n")
  book.write("\\begin{document}\n")
  book.write("\\begin{titlepage}\n")
  book.write("\\pagestyle{empty}\n")
  book.write("\\setcounter{page}{1}\n")
  book.write("\\centerline{\\LARGE\\bfseries \\'El\\'ements de g\\'eom\\'etrie alg\\'ebrique}\n")
  book.write("\\vskip0.5in\n")
  book.write("\\noindent\n")
  book.write("\\centerline{A.~Grothendieck and J.~Dieudonn\\'e}\n")
  book.write("\\centerline{Publications math\\'ematiques de l'I.H.\\'E.S}\n")
  book.write("\\vskip0.5in\n")
  book.write("\\noindent\n")
  book.write("\\centerline{\\bfseries Contributors}\n")
  book.write("\\centerline{")
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
    book.write(contributors)
  book.write("}\n")
  book.write("\\end{titlepage}\n")
  book.write("\\setcounter{tocdepth}{2}\n")
  book.write("\\tableofcontents\n")
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
          if line.find("\\chapter{}") == 0:
            line = ""
        if line.find("\\maketitle") == 0:
          continue
        if line.find("\\tableofcontents") == 0:
          continue
        if line.find("\\bibliography") == 0:
          continue
        if line.find("\\nocite{*}") == 0:
          continue
        if line.find("\\end{document}") == 0:
          continue
        book.write(line)
  book.write("\\bibliography{the}\n")
  book.write("\\bibliographystyle{amsalpha}\n")
  book.write("\\end{document}\n")

