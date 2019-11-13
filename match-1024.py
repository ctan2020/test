import sys,re

list={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line=ifile1.readline().strip()
		if not line:break
		nm=line.split()[0]
		list[nm]=line

ofile=open(sys.argv[3],"w")
with open(sys.argv[2]) as ifile2:
	while(2):
		line=ifile2.readline().strip()
		if not line:break
	#	nm=line.split()[0]
		mt=re.search("mips||([^|]*)|",line)
		if mt:
			nm=mt.group(1)
			if nm in list.keys():
				opt=list[nm]+"\t"+line+"\n"
				ofile.write(opt)
