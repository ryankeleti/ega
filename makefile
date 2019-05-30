# modified from https://github.com/stacks/stacks-project
# license at scripts/COPYING

LIJST = intro prelim schemes bibliography

LIJST_TAGS = $(LIJST) book

TEX = $(patsubst %,%.tex,$(LIJST))
TAGS = $(patsubst %,tags/tmp/%.tex,$(LIJST_TAGS))
TAG_EXTRAS = tags/tmp/my.bib tags/tmp/hyperref.cfg\
	tags/tmp/Makefile tags/tmp/chapters.tex\
	tags/tmp/preamble.tex tags/tmp/bibliography.tex
PDFS = $(patsubst %,%.pdf,$(LIJST))
PDFLATEX := pdflatex

.PHONY: default
default: $(TEX)
	@echo "make pdfs   --- makes all pdfs"
	@echo "make book   --- makes complete book pdf"
	@echo "make all    --- make pdfs + make book"

.PHONY: pdfs
pdfs: $(PDFS)

tmp/book.tex: *.tex
	python2 ./scripts/make_book.py "$(CURDIR)" > tmp/book.tex

book.pdf: tmp/book.tex
	$(PDFLATEX) tmp/book
	$(PDFLATEX) tmp/book

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*

tags/tmp/book.tex: tmp/book.tex tags/tags
	python2 ./scripts/tag_up.py "$(CURDIR)" book > tags/tmp/book.tex

tags/tmp/preamble.tex: preamble.tex tags/tags
	python2 ./scripts/tag_up.py "$(CURDIR)" preamble > tags/tmp/preamble.tex

tags/tmp/chapters.tex: chapters.tex
	cp chapters.tex tags/tmp/chapters.tex

tags/tmp/%.tex: %.tex tags/tags
	python2 ./scripts/tag_up.py "$(CURDIR)" $* > tags/tmp/$*.tex

tags/tmp/hyperref.cfg: hyperref.cfg
	cp hyperref.cfg tags/tmp/hyperref.cfg

tags/tmp/ega-bib.bib: ega-bib.bib
	cp ega-bib.bib tags/tmp/ega-bib.bib

tags/tmp/makefile: tags/makefile
	cp tags/makefile tags/tmp/makefile

.PHONY: tags
tags: $(TAGS) $(TAG_EXTRAS)
	$(MAKE) -C tags/tmp

.PHONY: tags_clean
tags_clean:
	rm -f tags/tmp/*
	rm -f tmp/book.tex

# Additional targets
.PHONY: book
book: book.pdf

.PHONY: clean
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc
	rm -f tmp/book.tex
	rm -i *.pdf

.PHONY: cleanall
cleanall: clean tags_clean

.PHONY: all
all: pdfs book

WEBDIR=../WEB
.PHONY: web
web:
	cp ega-bib.bib $(WEBDIR)/ega-bib.bib
	cp tagger.py $(WEBDIR)/tagger.py
	python2 ./scripts/web_book.py "$(CURDIR)" > $(WEBDIR)/book.tex
	cd $(WEBDIR) && python tagger.py && cd -


