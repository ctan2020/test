

import re,sys,os

from Bio import SeqIO

ofile=open(sys.argv[2],"w")
for fa in SeqIO.parse(sys.argv[1],"fasta"):
	n_num=fa.seq.count("N")
	if n_num<10:
		opt=">" +str(fa.id)+"\n"+str(fa.seq)+"\n"
		ofile.write(opt)
	
