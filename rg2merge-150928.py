
import sys,re

hd='''#!/bin/bash -l
module load gcc
module use /ivec/sles11sp3/modulefiles/bio-apps
module load samtools/1.1
samtools merge -f '''

list={}
with open(sys.argv[1]) as ifile:
	while(1):
		line =ifile.readline().strip()
		if not line:break
		reg = re.search("ID:(\S+)\sSM:(\S+)",line)
		id = reg.group(1)
		sm = reg.group(2)
		ofile=open(sm + "-merge.sh","a")
		if sm not in list.keys():
			list[sm] = 1
			opt = hd + " " + "../Alignment/" +sm + ".bam" + " " + "../Alignment/" + id + ".sam.bam" + " "
			ofile.write(opt)
		else:
			opt = "../Alignment/" + id + ".sam.bam" + " "
			ofile.write(opt)
			
			
			
		
