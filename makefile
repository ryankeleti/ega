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
	@echo "make pdfs  --- makes all pdfs"
	@echo "make book  --- makes complete book pdf"
	@echo "make all   --- make pdfs + make book"
	@echo "make clean --- clean up"

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
	if [ -d $(PDF_DIR) ]; then rm -ir $(PDF_DIR); fi
	for f in *.pdf; do if [ -f "$$f" ]; then rm -i *.pdf; fi; done

.PHONY: cleanforceall
cleanforceall:
	rm -f *.aux *.bbl *.blg *.log *.fdb_latexmk *.fls *.out *.toc *.pdf book.tex $(PDF_DIR)/*.pdf
	rmdir $(PDF_DIR)



.PHONY: all
all: pdfs book

