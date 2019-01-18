import glob
import re

#
# provided by Pieter Belmans, https://pbelmans.ncag.info/
#

path = "../ega/"
filename = path+"ega.tex"

# no I, no O
CHARACTERS = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"

# recursively read a TeX file
def read(filename):
  # \input doesn't have the .tex
  if filename[-4:] != ".tex":
    filename = filename + ".tex"

  tex = ""

  with open(filename) as f:
    for line in f:
      # remove comments
      line = line.split("%")[0]

      # look for \input's
      matches = re.findall("\\\\input{([^}]+)", line)
      for match in matches:
        line = line.replace("\\input{" + match + "}", read(match))

      tex = tex + line

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
  return tobase(i).rjust(4, "0")

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

# where we should start
i = last + 1

# list of used labels with a tag
old = []

# dictionary of newly assigned labels
new = dict()

tex = read(filename)
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
    i = i + 1

missing = [label for label in labels if label not in old]
if len(missing) > 0:
  print("The following labels are no longer present in the actual TeX file:")
  for label in missing:
    print(" - %s" % label)
  print("Not assigning tags until fixed.")
else:
  for label in new:
    print("%s,%s" % (new[label], label))

