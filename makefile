all: main

EGA=en.ega.main

main: en.ega.main

en.ega.main:
	pdflatex $(EGA).tex
	pdflatex $(EGA).tex

#WEBDIR=WEB
#web:
#	mkdir $(WEBDIR)/
#	cp $(EGAI).tex $(WEBDIR)/ega.tex
#	cp preamble.tex bib.tex $(WEBDIR)/
#	cd $(WEBDIR)/
#	python tagger.py > tags
#	plastex ega.tex

clean:
	rm -f $(EGA).aux $(EGA).bbl $(EGA).blg $(EGA).log $(EGA).out $(EGA).toc $(EGA).fls $(EGA).fdb_latexmk

cleanpdf:
	rm -f $(EGAI).pdf

#cleanweb:
#	rm -rf $(WEBDIR)

cleanall: clean cleanpdf #cleanweb

