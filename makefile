all: main

main:
	pdflatex main.tex
	pdflatex main.tex

web:
	sh comp-web.sh

clean:
	rm -f main.aux main.log main.out main.toc main.pdf

cleanweb:
	rm -rf WEB/


