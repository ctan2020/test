#!/group/ctan/anaconda3/envs/snakemake/bin/python3.6

import sys,os,re

sys.path.extend("/home/ctan/bin/")

import ctan as my

            
#my.extract_pos(sys.argv[1],sys.argv[2],sys.argv[3])

# my.genotype_from_vcf(sys.argv[1],sys.argv[2])

#my.chr2parts_bed(sys.argv[1],sys.argv[2])

my.parts2chr_vcf(sys.argv[1],sys.argv[2])

#my.vcf2summary(sys.argv[1],sys.argv[2])

#my.chr2parts_bed(sys.argv[1],sys.argv[2])

#extract_data(sys.argv[1],sys.argv[2])
				
#my.parts2chr(sys.argv[1],sys.argv[2])

#my.parts2chr_bim(sys.argv[1],sys.argv[2])

#my.parts2chr_bed(sys.argv[1],sys.argv[2])

#my.chr2parts(sys.argv[1],sys.argv[2])
