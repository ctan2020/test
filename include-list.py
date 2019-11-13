
import re,sys

ofile=open(sys.argv[3],"w")

list={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline()
		if not line:break
		one = line.split()[0]
		list[one]=1

with open(sys.argv[2]) as ifile2:
	while(1):
		line=ifile2.readline()
		if not line:break
		one = line.split()[0]
		if one in list.keys():
			ofile.write(line)
