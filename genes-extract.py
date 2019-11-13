import os,sys,re

def _genes_in_bed(genes,beds,ofile):
	for line in genes:
		lines=line.split()
		for one in beds:
			ones=one.split()
			if ones[0]==lines[0] and ones[1]<=lines[1] and ones[2]>=lines[2]:
				ofile.write(line)

def _genes_in_list(genes,list,ofile):
	for line in genes:
		for one in list:
			if one.split()[0] in line:
				ofile.write(line)

ifile1=open("/ref/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos.fun").readlines()
ifile2=open(sys.argv[1]).readlines()
ofile=open(sys.argv[2],"w")

#_genes_in_list(ifile1,ifile2,ofile)
_genes_in_bed(ifile1,ifile2,ofile)
