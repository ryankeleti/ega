# see README.md/COPYING.
import re

# find location of repository
def get_path():
  from sys import argv
  if not len(argv) == 2:
    print("\nThis script needs exactly one argument,")
    print("namely the path to the EGA directory\n")
    raise Exception('Wrong arguments')
  return argv[1].rstrip("/") + "/"

# assuming there is a title on the line, find it.
def find_title(line):
  n = line.find("\\title{")
  if n < 0:
    return ""
  n += 6
  m = find_sub_clause(line, n, "{", "}")
  title = line[n + 1 : m]
  return title

# returns all long labels for a given name
def get_all_labels(path, name):
  labels = []
  with open(path + name + ".tex", 'r') as f:
    for line in f:
      label = find_label(line)
      if label:
        label = name + "-" + label
        labels.append(label)
  return labels

# returns all long labels in the project
def all_labels(path):
  labels = []
  for name in list_text_files(path):
    labels += get_all_labels(path, name)
  return labels

def get_parts(path):
  listf = list_text_files(path)
  parts = {}
  with open(path + "chapters.md", 'r') as f:
    n = 0
    name = listf[n]
    for line in f:
      if line.find(name + "-section-phantom") >= 0:
        n += 1
        name = listf[n]
      if line.find('\\') < 0:
        title = line.rstrip()
        label = "book-part-" + "-".join(title.lower().split())
        parts[name] = [title, label]
  return parts

# list the stems of the TeX files in the project in the correct order
def list_text_files(path):
  with open(path + "makefile", 'r') as f:
    for line in f:
      n = line.find("FILES = ")
      if n == 0:
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

# find clause starting in specific spot with specific open and close characters
def find_sub_clause(text, spot, open, close):
  nr_braces = 0
  while nr_braces >= 0:
    spot += 1
    if text[spot] == open:
      nr_braces += 1
    if text[spot] == close:
      nr_braces -= 1
  return spot

# returns short label. Does not assume there is a label on the line
def find_label(env_text):
  n = env_text.find("\\label{")
  if n < 0:
    return ""
  n += 6
  m = find_sub_clause(env_text, n, "{", "}")
  label = env_text[n + 1 : m]
  return label

# silly function
def get_tag_line(line):
  line = line.rstrip()
  return line.split(",")

# get all active tags in the project
def get_tags(path, tagsfile):
  tags = []
  with open(path + tagsfile, 'r') as f:
    for line in f:
      if not line.find("#") == 0:
        tags.append(get_tag_line(line))
  return tags

# chapters unmodified
def print_chapters(path):
  with open(path + "chapters.md", 'r') as f:
    for line in f:
      print(line, end='')
  return

#
# modified from a script provided by Pieter Belmans, https://pbelmans.ncag.info/
# and the script web_book.py from https://github.com/stacks/stacks-project.
#

# no I, no O
CHARS = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"

# recursively read a TeX file
def readtex(filename):
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
        line = line.replace("\\input{" + match + "}", readtex(match))
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

def write_return_tags(path, infile, tagsfile):
  i = 0
  new = dict() # dictionary of newly assigned labels
  matches = re.findall("\\\\label{([^}]+)}", readtex(path + infile))
  for label in matches:
    tag = tobase(i).rjust(4, '0')
    if label.find("section-phantom") == 0:
      continue
    new[label] = tag
#debug    print("%s,%s" % (tag, label))
    i += 1
  with open(tagsfile, 'w+') as f:
    for label in new:
#debug        print("writing tag %s,%s" % (new[label], label))
      f.write(new[label] + "," + label + "\n")
  return new

