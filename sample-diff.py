######################################################
## indentify the samples with the same genoype
import os,sys,re

ifile1 = open(sys.argv[1]).readlines()
ifile2 = open(sys.argv[2]).readlines()
ofile = open(sys.argv[3],"w")
ofile2=open(sys.argv[4],"w")

del _sample_compare(ifile1,ifile2,ofile,ofile2):
	for i in range(1,len(ifile1)):
        	for j in range(1,len(ifile2)):
				lines1 = ifile1[i].split()
				lines2 = ifile2[j].split()
				sm=1
				for m in range(1,len(lines1)):
					if lines1[m] != "N" and lines2[m] !="N" and lines1[m] != lines2[m]:
						sm=0
				if sm ==1:
					opt =str(lines1[0]) + "\t" + str(lines2[0])+"\n"
					opt2=ifile1[i]+ifile2[j]+"\n"
					ofile.write(opt)
					ofile2.write(opt2)

ifile1 = open(sys.argv[1]).readlines()
ifile2 = open(sys.argv[2]).readlines()

ofile = open(sys.argv[3],"w")
ofile2=open(sys.argv[4],"w")

_sample_compare(ifile1,ifile2,ofile,ofile2)
