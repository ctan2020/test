
import os,re,sys

ofile=open(sys.argv[-1],"w")

list = {}
with open(sys.argv[1]) as ifile1:
	while(1):
		line = ifile1.readline()
		if not line:break
		lines = line.split()
		idx = lines[0] + ":" + lines[1] + "-" + lines[2]
		list[idx] = lines[3]

with open(sys.argv[2]) as ifile2:
	while(1):
		line = ifile2.readline()
		if not line:break
		if ">" in line:
			mt = re.match(">(chr.*)",line)
			idx = mt.group(1)
			if idx in list.keys():
				opt = line.strip() + "|" + list[idx] + "|Genomic sequence\n"
				ofile.write(opt)
		else:
			ofile.write(line)
