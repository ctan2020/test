import sys,os,re

ofile=open(sys.argv[3],"w")

repre={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline().strip()
		if not line:break
		lines=line.split()
		repre[lines[0]]=1

with open(sys.argv[2]) as ifile2:
	while(1):
		line=ifile2.readline()
		if not line:break
		mt=re.search("transcript_id\s\"(HORVU[A-Zr0-9.]*)\"",line)
		if mt and mt.group(1) in repre:
			ofile.write(line)
