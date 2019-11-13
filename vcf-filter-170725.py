#!/group/ctan/anaconda3/envs/snakemake/bin/python

import sys
from vcf_ctan import samvcf
from pysam import VariantFile

samples= ["AC","BD","Commander","EC2.1","EC2.2","EC7.1","EC7.2","Fleet","Hindmarsh","La_Trobe","Scope","Vlamingh","W1","WI4304","X1","barke","bowman","haruna_Nijo","igri","spontaneum_B1k-04-12"]
grp = ["bam/YSX-W_HJMFHALXX_L5.rmdup.bam","bam/TBT-M_HJMFHALXX_L4.rmdup.bam"]


ibcf = VariantFile(sys.argv[1])
#obcf = VariantFile(sys.argv[2],'w',header=ibcf.header)
ofile = open(sys.argv[2],"w")
hd = ["#chr","pos","len","ref","alt","gt_count"]
for one in grp:
    hd = hd + [one,"Reads"]
ofile.write("\t".join(hd) + "\n")
for one in ibcf.fetch():
    record = samvcf(one)
    if record.extract(grp):
        opt = record.opt + record.extract(grp)
        ofile.write("\t".join(opt) + "\n")

