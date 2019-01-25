all: main

main: en.main fr.main

en.main:
	pdflatex en.main.tex
	pdflatex en.main.tex

fr.main:
	pdflatex fr.main.tex
	pdflatex fr.main.tex

WEBDIR=WEB
web:
	mkdir $(WEBDIR)/
	cp main.tex $(WEBDIR)/ega.tex
	cp preamble.tex intro.tex bib.tex $(WEBDIR)/
	cd $(WEBDIR)/
#	python tagger.py > tags
	plastex ega.tex

clean:
	rm -f en.main.aux en.main.log en.main.out en.main.toc en.main.pdf
	rm -f fr.main.aux fr.main.log fr.main.out fr.main.toc fr.main.pdf

cleanweb:
	rm -rf $(WEBDIR)

cleanall: clean cleanweb

