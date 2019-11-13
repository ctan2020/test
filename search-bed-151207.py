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
		opt=""
		if ">" in line:
			mt=re.match(">(morex.+)$",line)
			nm=mt.group(1)
			if nm in list.keys():
				opt=">"+list[nm]+"|"+ nm +"\n"
		else:
			opt=line + "\n"
		ofile.write(opt)
