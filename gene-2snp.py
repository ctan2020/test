import sys,os,re

def _count(ifile,ofile):
	list={}
	for line in ifile:
		num=len(re.findall('1/1',line))
		lines = line.split()
		opt = str(line)
		if num<10:
			if lines[4] not in list:
				ofile.write(opt)
				list[lines[4]]=1
			elif list[lines[4]] < 3:
				ofile.write(opt)
				list[lines[4]]=list[lines[4]]+1
		
			
ifile=open(sys.argv[1]).readlines()
ofile=open(sys.argv[2],"w")

_count(ifile,ofile)
