#!/bin/python 

import re,sys,os,numpy

ifile = open(sys.argv[1]).readlines()
ofile = open(sys.argv[2],"w")

def indel_count(line):
	lines = line.split()
	count=[0]*4
	if "INS" in line:
		if lines[11]==lines[12] and lines[13]==lines[14]:
                	if lines[11]=="0/0" and lines[13]=="1/1":
				count[2]=1
                	elif lines[11]=="1/1" and lines[13]=="0/0":
				count[0]=1
	elif "DEL" in line:
		if lines[11]==lines[12] and lines[13]==lines[14]:
			if lines[11]=="0/0" and lines[13]=="1/1":
				count[3]=1
			elif lines[11]=="1/1" and lines[13]=="0/0":
				count[1]=1
	return count


list=[0]*4

for line in ifile:
	if not line.startswith("#"):
		rt = indel_count(line)
		for i in range(4):
			list[i]=list[i]+rt[i]
		
print(list)
