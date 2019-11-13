
import os,sys,re

ifile = open(sys.argv[1]).readlines()
ofile = open(sys.argv[2],"w")


def indel2csv(ifile,ofile):
	for line in ifile:
		lines = line.strip().split("\t")
		indel_id = "IND|"+lines[1]+"|"+str(lines[2]).zfill(9)
		opt = ",".join([indel_id]+lines[1:5]+[lines[0]]+[lines[5],lines[6]+"|"+lines[7]]+lines[8:28])+"\n"
		ofile.write(opt)

def snp2csv(ifile,ofile):
	for line in ifile:
		lines = line.strip().split("\t")
		snp_id = "SNP|" + lines[0]+"|"+str(lines[1]).zfill(9)
		opt = ",".join([snp_id]+lines[0:4]+["SNP",lines[4],lines[5]+"|"+lines[6]]+lines[7:27])
		ofile.write(opt)
snp2csv(ifile,ofile)
