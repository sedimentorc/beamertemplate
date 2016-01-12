all: abbreviations.bib prez.pdf

prez.tex: beamertemplate.tex
	cp beamertemplate.tex prez.tex

prez.pdf: prez.tex abbreviations.bib
	pdflatex prez
	biber prez
	biber prez
	pdflatex prez
	pdflatex prez
	
abbreviations.bib:
	python genabrv.py abbreviations.txt	
	

clean:
	rm *.pdf *.aux *.log prez.tex