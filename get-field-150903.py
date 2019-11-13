
#####################################################
##	extract special field in text file
#####################################################
import sys,re

ofile=open(sys.argv[2],"w")

with open(sys.argv[1]) as ifile:
	while(1):
		line = ifile.readline()
		if not line:break
		if not line.startswith("#"):
			mt=re.search(r"(MLOC_\d+\.\d)",line)
			if mt:
				opt=str(mt.group(1)) + "\n"
				ofile.write(opt)
		
