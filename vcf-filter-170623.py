import sys
from vcf_ctan import vcf_record

ofile = open(sys.argv[2],"w")

samples= ["AC","BD","Commander","EC2.1","EC2.2","EC7.1","EC7.2","Fleet","Hindmarsh","La_Trobe","Scope","Vlamingh","W1","WI4304","X1","barke","bowman","haruna_Nijo","igri","spontaneum_B1k-04-12"]
pt1 = samples[16]
pt2 = samples[11]
hd = "\t".join(["chr","pos","len","ref","ref_num","alt","alt_num",pt1,pt1+"_AD",pt2,pt2+"_AD"]) + "\n"
ofile.write(hd)

with open(sys.argv[1]) as ifile:
    while(1):
        one = ifile.readline()
        if not one:break
        if not one.startswith("#"):
            record = vcf_record(one)
            if record.filter() == 1 and abs(record.INDEL) >= 15 and record.diff(samples.index(pt1),samples.index(pt2)):
                opt = "\t".join(record.OPT + [record.GT[samples.index(pt1)],str(record.AD0[samples.index(pt1)])+","+ str(record.AD1[samples.index(pt1)])] + [record.GT[samples.index(pt2)],str(record.AD0[samples.index(pt2)])+","+str(record.AD1[samples.index(pt2)])]) + "\n"
                ofile.write(opt.replace("/","|"))
