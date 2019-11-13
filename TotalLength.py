#	get the total length of sequences

import sys

ofile = open(sys.argv[2],"w")

seq = 0
with open(sys.argv[1]) as ifile:
	while(1):
		line = ifile.readline()
		if not line: break
		if line.find(">"):
			seq = seq + len(line)
		else:
			next
ofile.write(str(seq))
