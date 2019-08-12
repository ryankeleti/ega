#
# modified from https://github.com/stacks/stacks-project
# license at scripts/COPYING.md
#
FILES = what intro prelim schemes
TEX = $(patsubst %,%.tex,$(FILES))
PDFS = $(patsubst %,%.pdf,$(FILES))
PDFLATEX := pdflatex

.PHONY: default
default: $(TEX)
	@echo "make pdfs       --- makes all pdfs"
	@echo "make book       --- makes complete book pdf"
	@echo "make all        --- make pdfs + make book"
	@echo "make clean      --- clean up"

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

.PHONY: clean
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc
	rm -i *.pdf
	rm -i book.tex

.PHONY: all
all: pdfs book

