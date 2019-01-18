import sys,re

path="../en.ega.i/"

prelim_path="sections/0-prelim/"
prelim=[
"prelim.1.header",
"prelim.1.0","prelim.1.1","prelim.1.2","prelim.1.3","prelim.1.4","prelim.1.5","prelim.1.6","prelim.1.7",
"prelim.2.header",
"prelim.2.1","prelim.2.2",
"prelim.3.header",
"prelim.3.1","prelim.3.2","prelim.3.3","prelim.3.4","prelim.3.5","prelim.3.6","prelim.3.7","prelim.3.8",
"prelim.4.header",
"prelim.4.1","prelim.4.2","prelim.4.3","prelim.4.4",
"prelim.5.header",
"prelim.5.1","prelim.5.2","prelim.5.3","prelim.5.4","prelim.5.5",
"prelim.6.header",
"prelim.6.1","prelim.6.2","prelim.6.3","prelim.6.4","prelim.6.5","prelim.6.6","prelim.6.7",
"prelim.7.header",
"prelim.7.1","prelim.7.2","prelim.7.3","prelim.7.4","prelim.7.5","prelim.7.6","prelim.7.7","prelim.7.8"
]

schemes_path="sections/1-schemes/"
schemes=[
"schemes.1.header",
"schemes.1.1","schemes.1.2","schemes.1.3","schemes.1.4","schemes.1.5","schemes.1.6","schemes.1.7",
"schemes.2.header",
"schemes.2.1","schemes.2.2","schemes.2.3","schemes.2.4","schemes.2.5",
"schemes.3.header",
"schemes.4.header",
"schemes.5.header",
"schemes.6.header",
"schemes.7.header",
"schemes.8.header",
"schemes.8.1","schemes.8.2","schemes.8.3",
"schemes.9.header",
"schemes.9.1","schemes.9.2","schemes.9.3","schemes.9.4","schemes.9.5","schemes.9.6",
"schemes.10.header",
]

prelim_title=[
"Rings of fractions",
  "Rings and Algebras",
  "Radical of an ideal. Nilradical and radical of a ring",
  "Modules and rings of fractions",
  "Functorial properties",
  "Change of multiplicative subset",
  "Change of ring",
  "Indentification of the module $M_f$ as an inductive limit",
  "Support of a module",
"Irreducible spaces. Noetherian spaces",
  "Irreducible spaces",
  "Noetherian spaces",
"Supplement on sheaves",
  "Sheaves with values in a category",
  "Presheaves on an open basis",
  "Gluing of sheaves",
  "Direct images of presheaves",
  "Inverse images of presheaves",
  "Constant sheaves and locally constant sheaves",
  "Inverse images of presheaves of groups or rings",
  "Sheaves on pseudo-discrete spaces",
"Ringed spaces",
  "Ringed spaces, sheaves of $\sheaf{A}$-modules, $\sheaf{A}$-algebras",
  "Direct image of an $\sheaf{A}$-module",
  "Inverse image of an $\sheaf{A}$-module",
  "Relation between direct and inverse images",
"Quasi-coherent and coherent sheaves",
  "Quasicoherent sheaves",
  "Sheaves of finite type",
  "Coherent sheaves",
  "Locally free sheaves",
  "Sheaves on a locally ringed space",
"Flatness",
  "Flat modules",
  "Change of ring",
  "Local nature of flatness",
  "Faithfully flat modules",
  "Restriction of scalars",
  "Faithfully flat rings",
  "Flat morphisms of ringed spaces",
"Adic rings",
  "Admissible rings",
  "Adic rings and projective limits",
  "Pre-adic Noetherian rings",
  "Quasifinite modules over local rings",
  "Rings of restricted formal series",
  "Completed rings of fractions",
  "Completed tensor products",
  "Topologies on modules of homomorphisms"
]

schemes_title=[
"Affine schemes",
  "The prime spectrum of a ring",
  "Functorial properties of prime spectra of rings",
  "Sheaf associated to a module",
  "Quasicoherent sheaves over a prime spectrum",
  "Coherent sheaves over a prime spectrum",
  "Functorial properties of quasicoherent sheaves over a prime spectrum",
  "Characterisation of morphisms of affine schemes",
"Preschemes and morphisms of preschemes",
  "Definition of preschemes",
  "Morphisms of preschemes",
  "Gluing of preschemes",
  "Local schemes",
  "Preschemes over a prescheme",
"Products of preschemes",
"Subpreschemes and immersion morphisms",
"Reduced preschemes; separation conditions",
"Finiteness conditions",
"Rational maps",
"Chevalley schemes",
  "Allied local rings",
  "Local rings of an integral scheme",
  "Chevalley schemes",
"Supplement on quasicoherent sheaves",
  "Tensor product of quasicoherent sheaves",
  "Direct image of a quasicoherent sheaf",
  "Extension of sections of quasicoherent sheaves",
  "Extension of quasicoherent sheaves",
  "Closed image of a prescheme; closure of a subprescheme",
  "Quasicoherent sheaves of algebras; change of structure sheaf",
"Formal schemes"
]

print "\\documentclass{book}"

with open(path+"webpackages.tex","r") as packages:
  print packages.read()
packages.close()

with open(path+"preamble.tex","r") as preamble:
  print preamble.read()
preamble.close()

#print "\\allowdisplaybreaks[1]"
print "\\begin{document}"
print "\\title{EGA I}"
print "\\author{A. Grothendieck \\& J. Dieudonn{\\'e}}"
print "\\begin{titlepage}"
print "\\pagestyle{empty}"
print "\\setcounter{page}{1}"
print "\\maketitle"
print "\\end{titlepage}"
print "\\newcommand{\\asttri}{***}"
#print "\\renewcommand{\\oldpage}{}"

print "\\input{"+path+"webabstract}"

print "\\part*{Introduction}"
print "\\input{"+path+"intro}"

print "\\clearpage"
print "\\setcounter{part}{-1}"

print "\\part{Preliminaries}"
print "\\label{0-prelim}"

if len(prelim_title)!=len(prelim):
  sys.exit("number of prelim titles != number of prelim files")

for filename,title in zip(prelim,prelim_title):
  if filename.find("header")>0:
    print "\\section{"+title+"}"
  else:
    print "\\subsection{"+title+"}"
  print "\\label{0-"+filename+"}"
  dirnum=re.search(r"\d+",filename).group()
  print "\\input{"+path+prelim_path+"prelim."+dirnum+"/"+filename+"}"

print "\\clearpage"
print "\\setcounter{subsection}{0}"
print "\\part{The language of schemes}"
print "\\label{1-schemes}"

print "\\section*{Summary}"
print "\\label{1-schemes.summary}"
print "\\input{"+path+schemes_path+"schemes.summary}"

if len(schemes_title)!=len(schemes):
  print len(schemes_title)
  print len(schemes)
  sys.exit("number of schemes titles != number of schemes files")

for filename,title in zip(schemes,schemes_title):
  if filename.find("header")>0:
    print "\\section{"+title+"}"
  else:
    print "\\subsection{"+title+"}"
  print "\\label{1-"+filename+"}"
  dirnum=re.search(r"\d+",filename).group()
  print "\\input{"+path+schemes_path+"schemes."+dirnum+"/"+filename+"}"

print "\\input{"+path+"bib}"
print "\\end{document}\n"

