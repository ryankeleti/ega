#
# modified from https://github.com/stacks/stacks-project
# license at scripts/COPYING
#
FILES = intro prelim schemes
TEX = $(patsubst %,%.tex,$(FILES))
PDFS = $(patsubst %,%.pdf,$(FILES))
PDFLATEX := pdflatex

.PHONY: default
default: $(TEX)
	@echo "make pdfs       --- makes all pdfs"
	@echo "make book       --- makes complete book pdf"
	@echo "make tags       --- make tags file for book"
	@echo "make all        --- make pdfs + make book"
	@echo "make clean      --- clean up"
	@echo "make clean_tags --- remove tags file"

.PHONY: pdfs
pdfs: $(PDFS)

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	bibtex $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*

.PHONY: book
book:
	python ./scripts/make_book.py "$(CURDIR)" > book.tex
	$(PDFLATEX) book
	$(PDFLATEX) book
	bibtex book
	$(PDFLATEX) book
	$(PDFLATEX) book

.PHONY: tags
tags:
	python ./scripts/tagger.py

.PHONY: clean
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc
	rm -i *.pdf
	rm -i book.tex

.PHONY: clean_tags
clean_tags:
	rm -f tags

.PHONY: all
all: pdfs book

