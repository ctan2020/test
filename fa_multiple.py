#!/usr/local/bin/python2.5

import os
import sys
from optparse import OptionParser
from Bio import SeqIO

usage = "usage: %prog fasta_file_in directory_out"
parser = OptionParser(usage)
(opts, args) = parser.parse_args()
dir_out = os.getcwd()

if len(args)<1:
    print "Error: Please enter at least one argument."
    print "See program_name.py --help"
    sys.exit()
elif len(args)==2:
    dir_out = args[1]
elif len(args)>2:
    print "error: Please enter up to 2 arguments."
    print "See program_name.py --help"
    sys.exit()

file_in = args[0]

for record in SeqIO.parse(open(file_in), "fasta"):
    f_out = os.path.join(dir_out,record.id+'.fasta')
    SeqIO.write([record],open(f_out,'w'),"fasta")
