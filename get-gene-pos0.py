import sys,re

ofile=open(sys.argv[3],"w")

list={}
with open(sys.argv[1]) as ifile1:
	while (1):
		line = ifile1.readline().strip()
		if not line: break
		if not line.startswith("#"):
			lines = line.split()
			gene = lines[2]
			list[gene]=1
		
with open(sys.argv[2]) as ifile2:
	while(1):
		line = ifile2.readline().strip()
		if not line: break
		if not line.startswith("#"):
			lines = line.split("\t")
			mt = re.search("\"(MLOC_\d+\.\d)\"",line)
			if mt:
				gene=mt.group(1)
				if gene in list.keys():
					opt = lines[0]+"\t"+lines[3]+"\t"+lines[4]+"\t"+gene+"\n"
					ofile.write(opt)
		

#transcript_id "MLOC_10023.7";		
