
#!/usr/bin/python
# developed by vitorpiro@gmail.com
# vpiro.wordpress.com
import sys, getopt
from Bio import SeqIO

ifile=''
ofile=''
quali=''
qualo=''

def help(): return ("Usage: %s -i input -o output -q quality_output [33,64]" % sys.argv[0])
try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:q:")
    if len(myopts) == 0:
        print(help())
        sys.exit(2)
except getopt.GetoptError as e:
    #print (str(e))
    print(help())
    sys.exit(2)
 
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    elif o == '-q':
		if a == '33':
			quali='fastq-illumina'
			qualo='fastq-sanger'
		elif a == '64':
			quali='fastq-sanger'
			qualo='fastq-illumina'
 
#fastq-illumina (PHRED+64): illumina  1.3 to 1.7
#fastq-sanger (PHRED+33): Illumina 1.8
SeqIO.convert(ifile, quali, ofile, qualo)
