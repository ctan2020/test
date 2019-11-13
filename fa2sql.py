from Bio import SeqIO
import os,sys,re

ofile=open(sys.argv[2],"w")
for seq_record in SeqIO.parse(open(sys.argv[1]), "fasta"):
	opt = ",".join(["",seq_record.id,"Protein",str(len(seq_record)),str(seq_record.seq)+"\n"])
	ofile.write(opt)
