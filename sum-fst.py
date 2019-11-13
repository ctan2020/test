
import sys,re,os

ifile = open(sys.argv[1])
total=1000000
fst = ifile.readlines()
for i in range(1,len(fst)-1):
	lines1 = fst[i].split()
	lines2 = fst[i+1].split()
	if int(lines2[1]) < int(lines1[2]) and lines2[1]>lines1[1]:
		reg = lines2[1]-lines1[1]
	elif int(lines2[1]) < int(lines1[2]) and lines2[1]<lines1[1]:
		reg 
	else:
		reg = int(lines1[2]) - int(lines1[1])
	total = total + reg
	
print total
