
import re,os,sys

# python KASP-primer-extract180914.py SNP-list180914-result.txt SNP-list180914-result.txt2

ifile=open(sys.argv[1],"r")
ofile=open(sys.argv[2],"w")

adr=["GAAGGTGACCAAGTTCATGCT","GAAGGTCGGAGTCAACGGATT"]
ifiles=ifile.read().split("AS Primer Picking Result for")

for one in ifiles:
	if "Oligo 1" in one:
		snp=re.search("(\dH\d*)\s",one).group(1)
		wtp=re.search("Wildtype \w+ Primer 5': ([ATCG]*)\s",one).group(1)
		mtp=re.search("Mutant \w+ Primer 5': ([ATCG]*)\s",one).group(1)
		ctp=re.search("Common \w+ Primer 5': ([ATCG]*)\s",one).group(1)
		ofile.write("\t".join([snp+"_FAM",adr[0]+wtp,"\n"]))
		ofile.write("\t".join([snp+"_VIC",adr[1]+mtp,"\n"]))
		ofile.write("\t".join([snp+"_C",ctp,"\n"]))

