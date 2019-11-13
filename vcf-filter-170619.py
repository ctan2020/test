import sys
from vcf_ctan import vcf_record

ifile = open(sys.argv[1]).readlines()
ofile = open(sys.argv[2],"w")

samples= ["AC","BD","Commander","EC2.1","EC2.2","EC7.1","EC7.2","Fleet","Hindmarsh","La_Trobe","Scope","Vlamingh","W1","WI4304","X1","barke","bowman","haruna_Nijo","igri","spontaneum_B1k-04-12"]

for one in ifile:
    if not one.startswith("#"):
        record = vcf_record(one)
        if record.filter == 1:
            if abs(record.INDEL) >= 10:
                opt = "\t".join(record.OPT) + "\n"
                opt = opt.replace("/","|")
                ofile.write(opt)
