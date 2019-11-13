import sys,os,re

hd="""##fileformat=VCFv4.1
##FILTER=<ID=PASS,Description="All filters passed">
##samtoolsVersion=0.1.19-44428cd
##reference=file:///gpfssan1/home/smoothly/Morex_final_IBSC/160404_barley_pseudomolecules_masked.fasta
##contig=<ID=chr1H,length=558535432>
##contig=<ID=chr2H,length=768075024>
##contig=<ID=chr3H,length=699711114>
##contig=<ID=chr4H,length=647060158>
##contig=<ID=chr5H,length=670030160>
##contig=<ID=chr6H,length=583380513>
##contig=<ID=chr7H,length=657224000>
##contig=<ID=chrUn,length=249774706>
##filter="DP > 5  QUAL > 50 MQ > 40"
##INFO=<ID=DP,Number=1,Type=Integer,Description="Raw read depth">
##INFO=<ID=DP4,Number=4,Type=Integer,Description="# high-quality ref-forward bases, ref-reverse, alt-forward and alt-reverse bases">
##INFO=<ID=MQ,Number=1,Type=Integer,Description="Root-mean-square mapping quality of covering reads">
##INFO=<ID=FQ,Number=1,Type=Float,Description="Phred probability of all samples being the same">
##INFO=<ID=AF1,Number=1,Type=Float,Description="Max-likelihood estimate of the first ALT allele frequency (assuming HWE)">
##INFO=<ID=AC1,Number=1,Type=Float,Description="Max-likelihood estimate of the first ALT allele count (no HWE assumption)">
##INFO=<ID=AN,Number=1,Type=Integer,Description="Total number of alleles in called genotypes">
##INFO=<ID=IS,Number=2,Type=Float,Description="Maximum number of reads supporting an indel and fraction of indel reads">
##INFO=<ID=AC,Number=A,Type=Integer,Description="Allele count in genotypes for each ALT allele, in the same order as listed">
##INFO=<ID=G3,Number=3,Type=Float,Description="ML estimate of genotype frequencies">
##INFO=<ID=HWE,Number=1,Type=Float,Description="Chi^2 based HWE test P-value based on G3">
##INFO=<ID=CLR,Number=1,Type=Integer,Description="Log ratio of genotype likelihoods with and without the constraint">
##INFO=<ID=UGT,Number=1,Type=String,Description="The most probable unconstrained genotype configuration in the trio">
##INFO=<ID=CGT,Number=1,Type=String,Description="The most probable constrained genotype configuration in the trio">
##INFO=<ID=PV4,Number=4,Type=Float,Description="P-values for strand bias, baseQ bias, mapQ bias and tail distance bias">
##INFO=<ID=INDEL,Number=0,Type=Flag,Description="Indicates that the variant is an INDEL.">
##INFO=<ID=PC2,Number=2,Type=Integer,Description="Phred probability of the nonRef allele frequency in group1 samples being larger (,smaller) than in group2.">
##INFO=<ID=PCHI2,Number=1,Type=Float,Description="Posterior weighted chi^2 P-value for testing the association between group1 and group2 samples.">
##INFO=<ID=QCHI2,Number=1,Type=Integer,Description="Phred scaled PCHI2.">
##INFO=<ID=PR,Number=1,Type=Integer,Description="# permutations yielding a smaller PCHI2.">
##INFO=<ID=QBD,Number=1,Type=Float,Description="Quality by Depth: QUAL/#reads">
##INFO=<ID=RPB,Number=1,Type=Float,Description="Read Position Bias">
##INFO=<ID=MDV,Number=1,Type=Integer,Description="Maximum number of high-quality nonRef reads in samples">
##INFO=<ID=VDB,Number=1,Type=Float,Description="Variant Distance Bias (v2) for filtering splice-site artefacts in RNA-seq data. Note: this version may be broken.">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=GL,Number=3,Type=Float,Description="Likelihoods for RR,RA,AA genotypes (R=ref,A=alt)">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="# high-quality bases">
##FORMAT=<ID=DV,Number=1,Type=Integer,Description="# high-quality non-reference bases">
##FORMAT=<ID=SP,Number=1,Type=Integer,Description="Phred-scaled strand bias P-value">
##FORMAT=<ID=PL,Number=G,Type=Integer,Description="List of Phred-scaled genotype likelihoods">
##bcftools_isecVersion=1.2+htslib-1.2.1
##bcftools_isecCommand=isec -n+3 -p 120 120C1.flt.vcf.gz 120C2.flt.vcf.gz 120C3.flt.vcf.gz 120T1.flt.vcf.gz 120T2.flt.vcf.gz 120T3.flt.vcf.gz
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	bam
"""


inf="AC1=2;AF1=1;DP=570;DP4=9,6,370,149;FQ=-282;MQ=60;PV4=0.39,0.06,1,1;RPB=-3.763138e+00;VDB=3.162038e-01"
frt="GT:PL:GQ"
nm="1/1:212,24,0:45"

ifile = open(sys.argv[1]).readlines()
ofile = open(sys.argv[2],"w")
ofile.write(hd)

for line in ifile:
	lines = line.split()
	opt = lines[0] + "\t" + lines[1] + "\t.\t" + lines[2] + "\t" + lines[3] + "\t50" + "\t.\t" + inf + "\t" + frt + "\t" + nm + "\n"
	ofile.write(opt)


