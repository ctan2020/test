#!/group/ctan/anaconda3/envs/snakemake/bin/python

import sys
from vcf_ctan import samvcf
from pysam import VariantFile

samples= ["AC","BD","Commander","EC2.1","EC2.2","EC7.1","EC7.2","Fleet","Hindmarsh","La_Trobe","Scope","Vlamingh","W1","WI4304","X1","barke","bowman","haruna_Nijo","igri","spontaneum_B1k-04-12"]
smps = [samples[3],samples[4],samples[5],samples[6]]

ibcf = VariantFile(sys.argv[1])
#obcf = VariantFile(sys.argv[2],'w',header=ibcf.header)
ofile = open(sys.argv[2],"w")
hd = "\t".join(["#chr","pos","len","ref","ref_num","alt","alt_num")
ofile.write(hd)
for one in ibcf.fetch("chr3H"):
    record = samvcf(one)
    if record.flt and record.diff_repeat(smps):
        opt = record.opt + [str(sum(one.samples[smps[0]]['GT'])),",".join(list(map(str,one.samples[smps[0]]['AD']))),str(sum(one.samples[smps[1]]['GT'])),",".join(list(map(str,one.samples[smps[1]]['AD']))),str(sum(one.samples[smps[2]]['GT'])),",".join(list(map(str,one.samples[smps[2]]['AD']))),str(sum(one.samples[smps[3]]['GT'])),",".join(list(map(str,one.samples[smps[3]]['AD'])))]
        ofile.write("\t".join(opt) + "\n")
