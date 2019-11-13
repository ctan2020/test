import os,sys,re

def _list_compare(list1,list2):
	lt1={}	#list1
	for i in list1:
		lt1[i]=1
	lt2={}	#list2
	for i in list2:
		lt2[i]=1

	comm={}	#overlap between list1 and list2
	for i in lt2:
		if i in lt1:
                        comm[i]=1

	only1={}	#unique in list1
	only2={}	#unique in list2
	for i in lt1:
		if i not in comm:
			only1[i]=1
	for i in lt2:
		if i not in comm:
			only2[i]=1
	return [only1,only2,comm]

ifile1=open(sys.argv[1]).readlines()
ifile2=open(sys.argv[2]).readlines()

ofile1=open("-".join(["temp",sys.argv[1],"only"]),"w")
ofile2=open("-".join(["temp",sys.argv[2],"only"]),"w")
ofile3=open("-".join(["temp",sys.argv[1],sys.argv[2],"comm"]),"w")

list=_list_compare(ifile1,ifile2)

ofile1.write("".join(list[0].keys()))
ofile2.write("".join(list[1].keys()))
ofile3.write("".join(list[2].keys()))

