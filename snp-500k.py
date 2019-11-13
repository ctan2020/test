
import sys,os,re

dt=250000
chr=""
pos=0

ofile=open(sys.argv[2],"w")
with open(sys.argv[1]) as ifile1:
	while(1):
		line = ifile1.readline()
		if not line:break
		if not line.startswith("#"):
			lines = line.split("\t")
			dt2=int(lines[1])-int(pos)
			if lines[0] == chr and dt2 > dt:
				pos = lines[1]
				ofile.write(line)
			elif lines[0]!=chr:
				chr=lines[0]
				pos=lines[1]
				ofile.write(line)
		elif line.startswith("#"):
			ofile.write(line)			
