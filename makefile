all: main

main:
	pdflatex main.tex
	pdflatex main.tex

clean:
	rm main.aux main.log main.out main.toc main.pdf


