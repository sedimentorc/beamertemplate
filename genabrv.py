from sys import argv

script, filename = argv

with open(filename) as f:
    content = f.readlines()

entries=[]
for line in content:
    if line[0]!='%':
        if line[-1]=='\n':
            line=line[0:-1]
        words=line.split('\t')
        #print(words)
        if len(words)==3:
             entries.append("\\step[fieldsource="+words[0]+", match={"+words[1]+"},replace={"+words[2]+"}]")

fullentries=["% % How to do abbreviations manually",
"% put this in the preamble",
"% this file is generated automatically from"+filename,
"\\DeclareSourcemap{%",
"  \\maps[datatype=bibtex]{",
"    % Journal abbreviations",
"    \\map{"]+entries+["    }",
"  }",
"}"]
f = open('abbreviations.bib','w')
for line in fullentries:
    print(line+'\r\n')
    f.write(line+'\r\n') # python will convert \n to os.linesep
f.close() 