#!/usr/bin/python

import os,sys
wd = os.getcwd()

ofile = open(sys.argv[1],"w")

for x in os.listdir(wd):
	dr = os.path.join(wd,x)
	if os.path.splitext(dr)[1] == ".fa":
		ifile = open(dr)
		opt = ifile.read()
		ifile.close()
		ofile.write(opt)
ofile.close()
	
