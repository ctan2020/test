#!/ctan01/anaconda3/bin/python3.6

import pysam,sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

qury=pysam.Fastafile("/home/ctan/data/ref/Hordeum_vulgare/barley/blast/160404_barley_pseudomolecules_masked.fasta")

ifile2=open(sys.argv[1]).readlines()
ofile=open(sys.argv[2],"w")

#qury=pysam.Fastafile(sys.argv[3])
for one in ifile2:
	ones=one.split()
	faseq=qury.fetch(ones[0],int(ones[1]),int(ones[2]))
	faid="_".join(ones)
	record=SeqRecord(Seq(faseq),id=faid,name="NAME",description="DESCRP")
	SeqIO.write(record,ofile,"fasta")
