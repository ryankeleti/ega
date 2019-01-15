all: main

main:
	pdflatex main.tex
	pdflatex main.tex

web:
	python2 makeweb.py >> web.tex
	plastex --renderer=Gerby web.tex

clean:
	rm main.aux main.log main.out main.toc main.pdf


