#!/home/ctan/anaconda3/envs/snakemake/bin/python
import sys
import os
hd='''#!/bin/bash -l

'''
ifile = open(sys.argv[1]).readlines()
oname0 = "all_"+sys.argv[1]
ofile0 = open(oname0,"a")
for a in range(0,len(ifile)):
	oname = "sub_"+str(a)+"_"+sys.argv[1]
	ofile = open(oname,"w")
	opt = hd + ifile[a]
	ofile.write(opt)
	opt2 = "sh  " + oname + " &\n"
	ofile0.write(opt2)
cmd = "sh "+oname0
#os.system(cmd)

