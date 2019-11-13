import sys,re

ofile = open(sys.argv[2],"w")

row=0
with open(sys.argv[1]) as ifile:
	while (1):
		line = ifile.readline()
		if not line:break
		if not line.startswith("#"):
			row=row+1
			lines = line.split()
			allel1=0
			allel2=0
			for x in range(0,len(lines)):
				if lines[x] == '0/0':
					allel1=allel1+2
				elif lines[x] == '0/1':
					allel1=allel1+1
					allel2=allel2+1
				elif lines[x] == '1/1':
					allel2=allel2+2
			opt=str(row)+"\t4\t2\t"+str(allel1)+"\t"+str(allel2)+"\n"
			ofile.write(opt)
