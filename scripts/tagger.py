#!/usr/bin/env python
import glob
import re

#
# modified from a script provided by Pieter Belmans, https://pbelmans.ncag.info/
# and the script web_book.py from https://github.com/stacks/stacks-project.
#

path = "./"
mainfile = path + "book.tex"

# no I, no O
CHARACTERS = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"

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
      # remove comments
      line = line.split("%")[0]
      # look for \input's
      matches = re.findall("\\\\input{([^}]+)", line)
      for match in matches:
        line = line.replace("\\input{" + match + "}", read(match))
      tex += line
  return tex

# convert integer to tag
def tobase(i):
  global CHARACTERS
  assert i >= 0
  if i < len(CHARACTERS):
    return CHARACTERS[i]
  else:
    return tobase(i // len(CHARACTERS)) + CHARACTERS[i % len(CHARACTERS)]

def totag(i):
  return tobase(i).rjust(4, '0')

# convert tag to integer
def toint(tag):
  global CHARACTERS
  return sum([CHARACTERS.index(tag[i]) * len(CHARACTERS)**(4-i-1) for i in range(4)])

tags = dict()
labels = dict()
inactive = []
try:
  with open("tags") as f:
    for line in f:
      # actual tag
      if not line.startswith("#"):
        tags[line.split(",")[0]] = line.strip().split(",")[1]
        labels[line.strip().split(",")[1]] = line.strip().split(",")[0]
      # check for inactive tags too
      elif len(line.split(",")) == 2 and len(line.split(",")[0]) == 4:
        inactive.append(line.split(",")[0])
except FileNotFoundError:
  pass

# determine last assigned tag
try:
  last = toint(sorted(list(tags.keys()) + inactive)[-1])
except IndexError:
  last = -1

i = last + 1 # where we should start
old = [] # list of used labels with a tag
new = dict() # dictionary of newly assigned labels
tex = read(mainfile)
matches = re.findall("\\\\label{([^}]+)}", tex)
for label in matches:
  # old label
  if label in labels:
    old.append(label)
  # new label
  else:
    tag = tobase(i).rjust(4, "0")
    new[label] = tag
    #print("%s,%s" % (tag, label))
    i += 1

missing = [label for label in labels if label not in old]
#if len(missing) > 0:
#  print("The following labels are no longer present in the actual TeX file:")
#  for label in missing:
#    print(" - %s" % label)
#  print("Not assigning tags until fixed.")
if False:
  pass
else:
  with open("tags", 'w+') as f:
    for label in new:
      #print("new tag %s,%s" % (new[label], label))
      f.write(new[label]+", "+label+"\n")

#def get_tag_line(line):
#  line = line.rstrip()
#  return line.split(",")

# get all active tags in the project
#def get_tags(path):
#  tags = []
#  with open(path + "tags", 'r') as f:
#    for line in f:
#      if not line.find("#") == 0:
#        tags.append(get_tag_line(line))
#  return tags

