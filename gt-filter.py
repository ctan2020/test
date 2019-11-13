
import os,sys,re

ofile = open (sys.argv[-1],"w")

with open(sys.argv[1]) as ifile:
	while(1):
		line = ifile.readline()
		if not line:break
		ref = re.findall("0\/0",line)
		alt = re.findall("1\/1",line)
		if len(alt)>=2 and len(alt) <8:
			ofile.write(line)
