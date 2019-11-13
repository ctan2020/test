
import re,sys

ofile=open(sys.argv[-1],"w")

list={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline()
		if not line:break
		one = line.split()[0] + str(line.split()[1])
		list[one]=1

with open(sys.argv[2]) as ifile2:
	while(1):
		line=ifile2.readline()
		if not line:break
		one = line.split()[0] + str(line.split()[1])
		if one in list.keys():
			ofile.write(line)
