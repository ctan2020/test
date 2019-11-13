import sys,re

ofile=open(sys.argv[2],"w")

with open(sys.argv[1]) as ifile:
	while(1):
		line=ifile.readline()
		if not line:break
		mt=re.search("(MLOC_\d+\.\d)",line)
		lines=line.split()
		opt=mt.group(1) + "\t" + lines[0] + "\t" + lines[3] + "\t" + lines[4] + "\n"
		ofile.write(opt)
