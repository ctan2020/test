
import re,sys,os,numpy

ifile = open(sys.argv[1]).readlines()
ofile = open(sys.argv[2],"w")


header="""
##############################################################################
##	usage:	compare the variants of each pair of accessions
##	example: python $0	<genotype: ><output: >
##	author:	tancong_2012@126.com
#############################################################################
"""
print header
com=numpy.zeros((8,8))
diff=numpy.zeros((8,8))

for line in ifile:
	if not line.startswith("#"):
		lines = line.split("\t")
		for i in range(9,len(lines)):
			for j in range(i,17):
				if lines[i] == lines[j] and lines[j]=="1|1":
					com[i-9,j-9]=com[i-9,j-9]+1
				if lines[i] == "1|1" and lines[j] == "0|0":
					diff[i-9,j-9]=diff[i-9,j-9]+1
				elif lines[i] == "0|0" and lines[j] == "1|1":
					diff[i-9,j-9]=diff[i-9,j-9]+1

print(com)
print(diff)
