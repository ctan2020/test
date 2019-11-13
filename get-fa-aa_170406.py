from Bio import SeqIO
import sys,os,re

ifile=open(sys.argv[1])
ifile2=open(sys.argv[2])
ofile=open(sys.argv[3],"w")

list={}
for one in ifile.readlines():
        if not one.startswith("#"):
                line=one.strip().split()
                list[line[0].upper()]=1

for one in SeqIO.parse(ifile2,"fasta"):
        mt=re.search("([_A-Za-z0-9]+).*\d*",one.id)
        if mt and mt.group(1).upper() in list:
                opt=">"+one.id+"\n"+one.seq+"\n"
                ofile.write(str(opt))

