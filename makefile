# modified from https://github.com/stacks/stacks-project
# see scripts/README.md
FILES = what intro ega0 ega1 ega2 ega3 ega4 ref
TEX = $(patsubst %,%.tex,$(FILES))
PDFS = $(patsubst %,%.pdf,$(FILES))
PDFLATEX = pdflatex
PDF_DIR = $(shell pwd)/pdfs
WEBNAME = ega

.PHONY: default
default: $(TEX)
	@echo "make pdfs       --- makes all pdfs"
	@echo "make book       --- makes complete book pdf"
	@echo "make all        --- make pdfs + make book"
	@echo "make auto       --- make all, but for server"
	@echo "make clean      --- clean up"
	@echo "make cleanaux   --- clean up auxiliary files"
	@echo "make cleanforce --- clean up everything without prompt"

.PHONY: pdfs
pdfs: $(PDFS)

%.pdf: %.tex
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	if [ $* != what ]; then bibtex $*; fi
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	mkdir -p $(PDF_DIR)
	mv $*.pdf $(PDF_DIR)

$(FILES): %: %.pdf

.PHONY: book
book:
	python3 ./scripts/make_book.py "$(CURDIR)"
	$(PDFLATEX) book
	$(PDFLATEX) book
	bibtex book
	$(PDFLATEX) book
	$(PDFLATEX) book
	mkdir -p $(PDF_DIR)
	mv book.pdf $(PDF_DIR)

.PHONY: cleanaux
cleanaux:
	rm -f *.aux *.bbl *.blg *.log *.fdb_latexmk *.fls *.out *.toc

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
	rm -f *.aux *.bbl *.blg *.log *.fdb_latexmk *.fls *.out *.toc *.pdf book.tex *-auto.tex
	rm -rf $(PDF_DIR)
	rm -rf tags $(WEBNAME).* $(WEBNAME)
	rm -rf plastex/ gerby-website/

.PHONY: all
all: pdfs book

.PHONY: auto
auto:
	python3 ./scripts/make_book.py "$(CURDIR)"
	cp book.tex book-auto.tex
	sed -i 's/\\end{titlepage}/\\vskip0.5in\\noindent\\centerline{\\tt autobuild~::~$(shell date -u +"%F %H:%M %Z"),~git~hash~::~$(shell git rev-parse --short HEAD)}\\end{titlepage}/' book-auto.tex
	mkdir -p $(PDF_DIR)
	$(PDFLATEX) book-auto
	$(PDFLATEX) book-auto
	bibtex book-auto
	$(PDFLATEX) book-auto
	$(PDFLATEX) book-auto
	mv book-auto.pdf $(PDF_DIR)
	for f in $(FILES); do\
	  cp "$$f".tex "$$f"-auto.tex;\
	  sed -i 's/\\maketitle/\\maketitle\\noindent\\centerline{\\tt autobuild~::~$(shell date -u +"%F %H:%M %Z"),~git~hash~::~$(shell git rev-parse --short HEAD)}\\\\/' "$$f"-auto.tex;\
	  $(PDFLATEX) "$$f"-auto;\
	  $(PDFLATEX) "$$f"-auto;\
	  bibtex "$$f"-auto;\
		$(PDFLATEX) "$$f"-auto;\
	  $(PDFLATEX) "$$f"-auto;\
	  mv "$$f"-auto.pdf $(PDF_DIR);\
	done
	rm -f *.aux *.bbl *.blg *.log *.fdb_latexmk *.fls *.out *.toc *-auto.tex

