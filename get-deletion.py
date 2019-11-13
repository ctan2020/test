import sys,re
ofile=open(sys.argv[2],"w")

with open(sys.argv[1]) as ifile:
	while(1):
		line =ifile.readline()
		if not line:break
		dele=len(line.split("\t")[3])-len(line.split("\t")[4])
		if (dele>0 and "N" not in line.split()[3]):
			opt =str(dele)+"\t"+line
			ofile.write(opt)
