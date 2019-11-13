#!/group/ctan/anaconda3/envs/snakemake/bin/python

import sys
from vcf_ctan import samvcf
from pysam import VariantFile

samples= ["AC","BD","Commander","EC2.1","EC2.2","EC7.1","EC7.2","Fleet","Hindmarsh","La_Trobe","Scope","Vlamingh","W1","WI4304","X1","barke","bowman","haruna_Nijo","igri","spontaneum_B1k-04-12"]
grp1 = [samples[1],samples[10],samples[15],samples[17]]
grp2 = [samples[2],samples[8],samples[9],samples[11],samples[16]]

ibcf = VariantFile(sys.argv[1])
#obcf = VariantFile(sys.argv[2],'w',header=ibcf.header)
ofile = open(sys.argv[2],"w")
hd = ["#chr","pos","len","ref","alt","gt_count"]
for one in grp1 + grp2:
    hd = hd + [one,"Reads"]
ofile.write("\t".join(hd) + "\n")
for one in ibcf.fetch("chr5H",544822373,546294499):
    record = samvcf(one)
    if record.diff_group(grp1,grp2):
        opt = record.opt + record.diff_group(grp1,grp2)
        ofile.write("\t".join(opt) + "\n")

