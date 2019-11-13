#!/group/ctan/anaconda3/envs/snakemake/bin/python

import sys
from vcf_ctan import samvcf
from pysam import VariantFile

ibcf = VariantFile(sys.argv[1])
obcf = VariantFile(sys.argv[2],'w',header=ibcf.header)

for one in ibcf.fetch():
    record = samvcf(one)
    if record.flt:
        obcf.write(one)
 #   if record.ft and abs(record.indel) >= 5 and record.diff(pt1,pt2):
 #       opt = record.opt + [str(sum(one.samples[pt1]['GT'])),",".join(list(map(str,one.samples[pt1]['AD']))),str(sum(one.samples[pt2]['GT'])),",".join(list(map(str,one.samples[pt2]['AD'])))]
 #       ofile.write("\t".join(opt) + "\n")
