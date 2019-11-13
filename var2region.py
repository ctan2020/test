############################################
## pick up variation in target region
#usage: $0 region.bed variation.vcf target-variation.vcf
import sys,re,os

ofile = open(sys.argv[3],"w")

list=[]
with open(sys.argv[1]) as ifile1:
	while(1):
		line = ifile1.readline()
		if not line:break
		lines = line.split()
		list.append(lines) 
idx=len(list)
with open(sys.argv[2]) as ifile2:
	while(1):
		line = ifile2.readline()
		if not line: break
		lines = line.split()
		for i in range(0,idx):
			if list[i][0] == lines[0] and int(list[i][1])<=int(lines[1]) and int(list[i][2]) >= int(lines[1]):
				opt = line
				ofile.write(opt)

