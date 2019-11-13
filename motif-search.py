
import sys,os,re

#ofile = open(sys.argv[-1],"w")


with open(sys.argv[1]) as ifile:
	while(1):
		line = ifile.readline().strip()
		if not line:break
		mt = re.match("(CTT[ATCG]AAAGC[ATCG]A)",line)
		if mt:
			print mt.group(1)
		else:
			print "no\n"
