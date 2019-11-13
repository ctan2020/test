import sys,re

ofile=open(sys.argv[2],"w")
eff = ("missense_variant","start_lost","stop_lost","stop_gained")
list={}

with open(sys.argv[1]) as ifile1:
	while (1):
		line = ifile1.readline().strip()
		if not line: break
		lines = line.split("\t")
		mt = re.search(r"(MLOC_\d+\.\d)",line)
		mt2 = re.search("EFF=([^(]+)\(",line)
		if mt and mt2:
			gene=mt.group(1)
			mut=mt2.group(1)
			E21=re.search("(./.)",lines[13]).group(1)
			E22=re.search("(./.)",lines[14]).group(1)
			E71=re.search("(./.)",lines[15]).group(1)
			E72=re.search("(./.)",lines[16]).group(1)
			if E21 == E22 and E71 == E72 and E21 !=E71 and mut in eff:
				if gene not in list.keys():
					opt=lines[0]+"\t"+lines[1]+"\t"+gene+"\t"+mut+"\n"
					ofile.write(opt)
					list[gene]=1
