import os

path='./'

print "\\documentclass{book}"

packages=open(path+'webpackages.tex')
for line in packages:
  print line
packages.close()

preamble=open(path+'preamble.tex')
for line in preamble:
  print line
preamble.close()

print "\\begin{document}"
print "\\begin{titlepage}"
print "\\pagestyle{empty}"
print "\\setcounter{page}{1}"
print "\\centerline{\\LARGE\\bfseries EGA I}"
print "\\centerline{A. Grothendieck \& J. Dieudonn{\'e}}"
print "\\end{titlepage}"

#for root,direc,files in os.walk(path+'sections/'):
#  for filename in files: 
#    print os.path.join(root,filename)

print "\\input{"+path+"abstract.tex}"

inputs=open(path+'main-input.tex')
for line in inputs:
  print line
inputs.close()

print "\\input{"+path+"bib.tex}"
print "\\end{document}"

