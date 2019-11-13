import os,sys,re

def _genes_in_vcf(ifile,ofile):
	"""
	extract genes in vcf file
	"""
	with open(ifile1) as vcfs:
                while(1):
                        line = vcfs.readline()
			if not line: break
                        if not line.startswith("#"):
                                mt = re.search("(HORVU[0-9A-Za-z]+)",line)
				if mt:
					opt=mt.group(1)+"\n"
					ofile.write(opt)


def _vcf_in_genes(ifile1,genes,ofile):
	""""
	extract vcf records in genes
	"""
	dict_genes={}
	for i in genes:
		dict_genes[i.split()[0]]=1
	
	with open(ifile1) as vcfs:
		while(1):
			line = vcfs.readline()
			if not line.startswith("#"):
				mt = re.search("(HORVU[0-9A-Za-z]+)",line)
				if mt and mt.group(1) in dict_genes:
					ofile.write(line)

def _vcf_in_beds(ifile1,beds,ofile):
	"""
	extract vcf records in beds
	"""
	list_bed=[]
	for bed in beds:
		one = bed.split()
		list_bed.append(one)
	idx=len(list_bed)
	with open(ifile1) as vcfs:
		while(1):
			line = vcfs.readline()
			if not line:break
			if not line.startswith("#"):
				lines = line.split()
				for i in range(0,idx):
					if list_bed[i][0]==lines[0] and int(list_bed[i][1]) <= int(lines[1]) and int(list_bed[i][2]) >= int(lines[1]):
						ofile.write(line)

ifile1=sys.argv[1]
ifile2=open(sys.argv[2]).readlines()

ofile=open(sys.argv[3],"w")

#_genes_in_vcf(ifile1,ofile)

_vcf_in_beds(ifile1,ifile2,ofile)
