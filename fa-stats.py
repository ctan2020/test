
from Bio import SeqIO
import os,sys,re

ofile=open(sys.argv[2],"w")

total=0

for fa in SeqIO.parse(sys.argv[1],"fasta"):
	falen=len(fa.seq)
	rt=[fa.id,str(falen)]
	opt="\t".join(rt)+"\n"
	ofile.write(opt)
	total=total+falen
smy="\t".join(["Total",str(total)])+"\n"
ofile.write(smy)
