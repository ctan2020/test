import os,sys

from Bio import SeqIO

of1=open(sys.argv[2],"w")
of2=open(sys.argv[3],"w")
for record in SeqIO.parse(sys.argv[1], "fasta"):
	if "/1" in str(record.id):
		SeqIO.write(record,of1, "fasta")
	elif "/2" in str(record.id):
		SeqIO.write(record,of2, "fasta")


