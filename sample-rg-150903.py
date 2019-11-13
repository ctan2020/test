

##############################
##	produce rg file
##############################

import sys,re

ofile=open(sys.argv[2],"w")

SM=""
ID=""
PL="illumina"
LB=""
PU=""

with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline().strip()
		if not line:break
		if "CleanData" in line:
			mt=re.match(r'^(\S+)\/(\S+)\/CleanData',line)
			PU=mt.group(1)
			SM=mt.group(2)
		elif "1.fq" in line:
			ID=line.split("_1.")[0]
			LB=line.split("_")[4]
			opt="ID:"+ID+"\tSM:"+SM+"\tPL:"+PL+"\tLB:"+LB+"\tPU:"+PU+"\n"
			ofile.write(opt)
				
