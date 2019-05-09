all: main

EGAI=en.ega.i

main: en.ega.i.main

en.ega.i.main:
	pdflatex $(EGAI).tex
	pdflatex $(EGAI).tex

#WEBDIR=WEB
#web:
#	mkdir $(WEBDIR)/
#	cp $(EGAI).tex $(WEBDIR)/ega.tex
#	cp preamble.tex bib.tex $(WEBDIR)/
#	cd $(WEBDIR)/
#	python tagger.py > tags
#	plastex ega.tex

clean:
	rm -f $(EGAI).aux $(EGAI).bbl $(EGAI).blg $(EGAI).log $(EGAI).out $(EGAI).toc

cleanpdf:
	rm -f $(EGAI).pdf

#cleanweb:
#	rm -rf $(WEBDIR)

cleanall: clean cleanpdf #cleanweb

