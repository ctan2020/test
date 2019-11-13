#!/ctan01/anaconda3/bin/python3.6

import pysam,sys

chr=sys.argv[1]
pos=sys.argv[2]
start=int(pos)-250
end=int(pos)+300
ref=pysam.Fastafile("/ctan02/ref/barley/blast/160404_barley_pseudomolecules_masked.fasta")
seq=ref.fetch(chr,start,end)
print(seq)
