import sys,re

list={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline().strip()
		if not line:break
		nm=line.split()[1] + ":" + line.split()[2] + "-" + line.split()[3] 
		list[nm]=line.split()[0]

ofile=open(sys.argv[3],"w")
with open(sys.argv[2]) as ifile2:
	while(2):
		line=ifile2.readline().strip()
		if not line:break
		if ">" in line:
			nm=line.split()[0]
			if nm in list.keys():
				opt=list[nm]+"|"+line+"\n"
		else:
			opt=line
		ofile.write(opt)
