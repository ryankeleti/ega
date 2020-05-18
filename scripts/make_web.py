#!/usr/bin/env python
# see README.md/COPYING.md.
import re

out = "ega-web"

# get location of repo.
def get_path():
  from sys import argv
  if not len(argv) == 2:
    print("\nThis script needs one argument, the path to the EGA directory.\n")
    raise Exception('Wrong arguments')
  return argv[1].rstrip("/") + "/"

# list the stems of the TeX files in the project in the correct order.
def list_text_files(path):
  with open(path + "Makefile", 'r') as f:
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
  listf = listf.replace("what ", "")
  listf = listf.replace("intro ", "")
  return listf.split()

def rm_oldpage(line):
  line = re.sub(r"\\oldpage{.*?}\n", "", line)
  line = re.sub(r"\\oldpage\[.*?]{.*?}\n", "", line)
  line = re.sub(r"\\oldpage{.*?}", "", line)
  line = re.sub(r"\\oldpage\[.*?]{.*?}", "", line)
  return line

def convert_symb(line):
  line = re.sub(r"<", r"\\lt ", line)
  line = re.sub(r">", r"\\gt ", line)
  return line

def convert_sref(line):
  line = re.sub(r"\\hyperref\[section:(.*?)\]{.*?}", r"\\ref{section:\1}", line)
  line = re.sub(r"\\hyperref\[subsection:(.*?)\]{.*?}", r"\\ref{subsection:\1}", line)
  line = re.sub(r"\\eref", r"\\ref", line)
  line = re.sub(r"\\sref\[.*?\]", r"\\sref", line)
  line = re.sub(r"\\sref{(.*?)}\[(.*?)\]", r"\\sref{\1}, (\2)", line)
  line = re.sub(r"\\sref", r"\\ref", line)
  return line

def convert_sectioning(line):
  if line.find("\\title{Preliminaries") == 0:
    line = line.replace("\\title{Preliminaries", "\\setcounter{chapter}{-1}\\chapter{Preliminaries")
  line = re.sub(r"\\title{", r"\\chapter{", line)
  line = re.sub(r"\\chapter{}", "", line)
  return line

path = get_path() 
with open(path + out + ".tex", 'w') as book:
  with open(path + "preamble-web.tex", 'r') as preamble:
    for line in preamble:
      if line.find("%") == 0:
        continue
      if line.find("\\input{") == 0:
        x = re.search("input{(.+?)}", line).group(1)
        with open(x + ".tex", 'r') as ff:
          for ffline in ff:
            book.write(ffline)
        continue
      book.write(line)
  book.write("\\begin{document}\n")
  for name in list_text_files(path):
    with open(path + name + ".tex", 'r') as f:
      for line in f:
        if line.find("%") == 0:
          continue
        if line.find("\\input{preamble}") == 0:
          continue
        if line.find("\\begin{document}") == 0:
          continue
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
        if line.find("longtable") >= 0:
          continue
        line = re.sub(r"~", " ", line)
        line = rm_oldpage(line)
        line = convert_symb(line)
        line = convert_sref(line)
        line = convert_sectioning(line)
        if line.find("\\input{") == 0:
          x = re.search("input{(.+?)}", line).group(1)
          with open(x + ".tex", 'r') as ff:
            for ffline in ff:
              ffline = re.sub(r"~", " ", ffline)
              ffline = rm_oldpage(ffline)
              ffline = convert_symb(ffline)
              ffline = convert_sref(ffline)
              ffline = convert_sectioning(ffline)
              if ffline.find("longtable") >= 0:
                continue
              book.write(ffline)
          continue
        book.write(line)
  book.write("\\bibliography{the}\n")
  book.write("\\bibliographystyle{amsalpha}\n")
  book.write("\\end{document}\n")

