all: main

main:
	pdflatex main.tex
	pdflatex main.tex

web:
	cp main.tex web.tex
	python tagger.py > tags
	plastex --renderer=Gerby web.tex

clean:
	rm -f main.aux main.log main.out main.toc main.pdf

cleanweb:
	rm -rf web/ tags web.tex


