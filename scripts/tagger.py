#!/usr/bin/env python
import re

#
# modified from a script provided by Pieter Belmans, https://pbelmans.ncag.info/
# and the script web_book.py from https://github.com/stacks/stacks-project.
#
path = "./"
mainfile = path + "book.tex"

# no I, no O
CHARS = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"

# recursively read a TeX file
def read(filename):
  # \input doesn't have the .tex
  if filename[-4:] != ".tex":
    filename += ".tex"
  tex = ""
  with open(filename) as f:
    for line in f:
      if line.find("\\begin{document}") == 0:
        continue
      if line.find("\\title{") == 0:
        continue
      if line.find("\\maketitle") == 0:
        continue
      if line.find("\\tableofcontents") == 0:
        continue
      if line.find("\\clearpage") == 0:
        continue
      if line.find("\\end{document}") == 0:
        continue
      line = line.split("%")[0] # remove comments
      matches = re.findall("\\\\input{([^}]+)", line) # look for \input's
      for match in matches:
        line = line.replace("\\input{" + match + "}", read(match))
      tex += line
  return tex

# convert integer to tag
def tobase(i):
  global CHARS
  assert i >= 0
  if i < len(CHARS):
    return CHARS[i]
  else:
    return tobase(i // len(CHARS)) + CHARS[i % len(CHARS)]

def totag(i):
  return tobase(i).rjust(4, '0')

# convert tag to integer
def toint(tag):
  global CHARS
  return sum([CHARS.index(tag[i]) * len(CHARS)**(4-i-1) for i in range(4)])

i = 0
new = dict() # dictionary of newly assigned labels
matches = re.findall("\\\\label{([^}]+)}", read(mainfile))
for label in matches:
  tag = tobase(i).rjust(4, '0')
  if label.find("section-phantom") == 0:
    continue
  new[label] = tag
  print("%s,%s" % (tag, label))
  i += 1

with open("tags", 'w+') as f:
  for label in new:
    print("writing tag %s,%s" % (new[label], label))
    f.write(new[label] + "," + label + "\n")

def get_tag_line(line):
  line = line.rstrip()
  return line.split(",")

# get all active tags in the project
def get_tags(path):
  tags = []
  with open(path + "tags", 'r') as f:
    for line in f:
      if not line.find("#") == 0:
        tags.append(get_tag_line(line))
  return tags

