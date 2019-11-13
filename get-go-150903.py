
########################
##	get GO annotation
#########################

import sys

ofile=open(sys.argv[3],"w")

list={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline().strip()
		if not line: break
		list[line]=1

last=""			
with open(sys.argv[2]) as ifile2:
	while(1):
		line=ifile2.readline().strip()
		if not line:break
		lines=line.split()
		if lines[0] in list.keys():
			if lines[0] == last:
					opt="\t"+lines[1]
					ofile.write(opt)
			else:
					opt="\n"+lines[0]+"\t"+lines[1]
					ofile.write(opt)
					last=lines[0]
					
		
