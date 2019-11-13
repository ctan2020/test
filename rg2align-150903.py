
#################################
## produce align script from rg informaiton
#################################

import sys,re

hd='''#!/bin/bash -l
module load gcc
module use /ivec/sles11sp3/modulefiles/bio-apps
module load bwa/0.7.9a

'''
ref="/scratch/partner1006/ctan/ref-150901/BWA/150831_barley.fa"

with open(sys.argv[1]) as ifile:
	while(1):
		line=ifile.readline()
		if not line:break
		line.strip()
		if line:
			lines=line.split()
			ID=line.split()[0].split(":")[1]
			SM=line.split()[1].split(":")[1]
			rg="@RG\\t"+lines[0]+"\\t"+lines[1]+"\\t"+lines[2]+"\\t"+lines[3]+"\\t"+lines[4]
			with open(ID+"_align.sh","w") as ofile:
				opt=hd+"bwa mem -M -t 20  -R \'" + rg + "\' "+ref+" ../CleanData/"+str(SM)+"/"+str(ID)+"_1.fq.gz ../CleanData/"+str(SM)+"/"+str(ID)+"_2.fq.gz "+">\t../Alignment/"+str(ID)+".sam\n"
				ofile.write(opt)
