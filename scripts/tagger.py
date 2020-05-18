#!/usr/bin/env python
# modified from https://github.com/gerby-project/hello-world/tagger.py
import re

# no I, no O.
CHARACTERS = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"

# get location of repo.
def get_file():
  from sys import argv
  if not len(argv) == 2:
    print("\nThis script needs one argument, the file to be tagged.\n")
    raise Exception('Wrong arguments')
  return argv[1].rstrip(".tex")

FNAME = get_file()
filenames = [FNAME + ".tex"]

# convert integer to tag.
def tobase(i):
  global CHARACTERS
  assert i >= 0
  if i < len(CHARACTERS):
    return CHARACTERS[i]
  else:
    return tobase(i // len(CHARACTERS)) + CHARACTERS[i % len(CHARACTERS)]

def totag(i):
  return tobase(i).rjust(4, "0")

# convert tag to integer.
def toint(tag):
  global CHARACTERS
  return sum([CHARACTERS.index(tag[i]) * len(CHARACTERS)**(4-i-1) for i in range(4)])

tags = dict()
labels = dict()
inactive = []
try:
  with open("tags") as f:
    for line in f:
      # actual tag.
      if not line.startswith("#"):
        tags[line.split(",")[0]] = line.strip().split(",")[1]
        labels[line.strip().split(",")[1]] = line.strip().split(",")[0]
      # check for inactive tags too.
      elif len(line.split(",")) == 2 and len(line.split(",")[0]) == 4:
        inactive.append(line.split(",")[0])
except FileNotFoundError:
  pass

# determine last assigned tag.
try:
  last = toint(sorted(list(tags.keys()) + inactive)[-1])
except IndexError:
  last = -1

i = last + 1
for filename in filenames:
  with open(filename) as f:
    # do this line per line to deal with comments.
    for line in f:
      matches = re.findall("\\\\label{([^}]+)}", line.split("%")[0])
      for label in matches:
        if not label in labels:
          tag = tobase(i).rjust(4, "0")
          print("%s,%s" % (tag, label))
          i += 1

