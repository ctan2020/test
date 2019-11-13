import sys,os,re
# contanct:tancong_2012@hotmail.com
# cmd: python genotype2vcf.py wangrong-test.txt test.vcf

header="""##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##FORMAT=<ID=AD,Number=R,Type=Integer,Description="Allelic depths for the ref and alt alleles in the order listed">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth (reads with MQ=255 or with bad mates are filtered)">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=PL,Number=G,Type=Integer,Description="Normalized, Phred-scaled likelihoods for genotypes as defined in the VCF specification">
##contig=<ID=chr1H,length=558535432>
##contig=<ID=chr2H,length=768075024>
##contig=<ID=chr3H,length=699711114>
##contig=<ID=chr4H,length=647060158>
##contig=<ID=chr5H,length=670030160>
##contig=<ID=chr6H,length=583380513>
##contig=<ID=chr7H,length=657224000>
##contig=<ID=chrUn,length=249774706>
"""

ifl1=open(sys.argv[1]).readlines()
ofl1=open(sys.argv[2],"w")

ohd=ifl1[0].split()
opt=header+"\t".join(["#CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO","FORMAT"])+"\t"+"\t".join(ohd[6:]) +"\n"
ofl1.write(opt)


for one in ifl1[1:]:
	record=[]
	ones=one.split()
	record.extend(ones[4:6])
	record.append(ones[0])
	mt=re.search("([ATCG])>([ATCG])",ones[0])
	if mt:
		record.append(mt.group(1))
		record.append(mt.group(2))
	record.append("\t".join([".",".","."]))
	record.append("GT:GQ")
	gt="\t".join(ones[6:])
	gt=gt.replace("0","0/0:.")
	gt=gt.replace("1","1/1:.")
	gt=gt.replace("2","0/1:.")
	gt=gt.replace("-","./.:.")
	opt="\t".join([str(ele) for ele in record])+"\t"+gt+"\n"
	ofl1.write(opt)
	
