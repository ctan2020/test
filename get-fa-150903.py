
#####################################################
##	extract gene sequence from gene fasta file
#####################################################
import sys,re

list={}
ofile=open(sys.argv[3],"w")

with open(sys.argv[1]) as ifile1:
	while(1):
		line = ifile1.readline().strip()
		if not line:break
		if not line.startswith("#"):
			line.rstrip()
			list[line]=1

with open(sys.argv[2]) as ifile2:
	while(1):
		line = ifile2.readline().strip()
		if not line:break
		seq = ifile2.readline().strip()
		if not line.startswith("#"):
			mt=re.search("(MLOC_\d+\.\d)",line)
			if mt and mt.group(1) in list:
				opt=">"+str(mt.group(1))+"\n"+seq+"\n"
				ofile.write(opt)	
