

import sys,os,re

#pos="/brldata/home/ctan/ref/anno/psedo-gene-position.txt"
pos="/home/ctan/data/ref/Hordeum_vulgare/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos"

ofile = open(sys.argv[2],"w")

gene = {}
with open(pos) as ifile1:
	while(1):
		line=ifile1.readline()
		if not line:break
		lines = line.split()
		gene[lines[3]] = line
		
with open(sys.argv[1]) as ifile2:
	while(1):
		line = ifile2.readline()
		if not line:break
		lines = line.split()
		if lines[0] in gene.keys():
			opt = gene[lines[0]]
			ofile.write(opt)
