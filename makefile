#
# modified from https://github.com/stacks/stacks-project
# license at scripts/COPYING.md
#
FILES = what intro prelim schemes morphisms cohomology
TEX = $(patsubst %,%.tex,$(FILES))
PDFS = $(patsubst %,%.pdf,$(FILES))
PDFLATEX = pdflatex
PDF_DIR = $(shell pwd)/pdfs

.PHONY: default
default: $(TEX)
	@echo "make pdfs       --- makes all pdfs"
	@echo "make book       --- makes complete book pdf"
	@echo "make all        --- make pdfs + make book"
	@echo "make clean      --- clean up"
	@echo "make cleanforce --- clean up everything without prompt"

.PHONY: pdfs
pdfs: $(PDFS)

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	bibtex $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	mkdir -p $(PDF_DIR)
	mv $*.pdf $(PDF_DIR)

$(FILES): % : %.pdf

.PHONY: book
book:
	python ./scripts/make_book.py "$(CURDIR)" > book.tex
	$(PDFLATEX) book
	$(PDFLATEX) book
	bibtex book
	$(PDFLATEX) book
	$(PDFLATEX) book
	mkdir -p $(PDF_DIR)
	mv book.pdf $(PDF_DIR)

.PHONY: clean
clean:
	rm -f *.aux *.bbl *.blg *.log *.fdb_latexmk *.fls *.out *.toc
	if [ -f book.tex ]; then rm -i book.tex; fi
	for f in *.pdf; do if [ -f "$$f" ]; then rm -i *.pdf; fi; done
	if [ -d $(PDF_DIR) ]; then\
	  for f in $(PDF_DIR)/*.pdf; do\
	    if [ -f "$$f" ]; then rm -i $(PDF_DIR)/*.pdf; fi;\
	    break;\
	  done;\
	  rm -ir $(PDF_DIR);\
	fi

.PHONY: cleanforce
cleanforce:
	rm -f *.aux *.bbl *.blg *.log *.fdb_latexmk *.fls *.out *.toc *.pdf book.tex
	rm -rf $(PDF_DIR)

.PHONY: all
all: pdfs book

