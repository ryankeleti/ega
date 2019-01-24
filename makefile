all: main

main:
	pdflatex main.tex
	pdflatex main.tex

WEBDIR=WEB
web:
	mkdir $(WEBDIR)/
	cp main.tex $(WEBDIR)/ega.tex
	cp preamble.tex intro.tex bib.tex $(WEBDIR)/
	cd $(WEBDIR)/
#	python tagger.py > tags
	plastex ega.tex

clean:
	rm -f main.aux main.log main.out main.toc main.pdf

cleanweb:
	rm -rf $(WEBDIR)

cleanall: clean cleanweb

