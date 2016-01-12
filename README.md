# Features

- metropolis beamer
- logos on title page
- animate to embed videos frame by frame and autoplay
- video playing externally
- biblatex for citations
- journal abbreviation rules (manual input of rules into text files, but automated assembly into latex code, see genabrv.py)
- custom biblatex commands for footnote citations
- multi-page bibliography




# How-to

1. run imagesfromvideo.sh to generate the images for animate
2. edit graphicspath in tex file to ensure it's it's pointing to the folders you want
3. compile pdflatex using linux machine. Use the makefile. You can probably get this to work on Windows.
4. Play using adobe acrobat in windows. Neither animate nor playing videos externally work seamlessly for me in linux. Unfortunate, because if it did, you could use the pdfpc presenter.