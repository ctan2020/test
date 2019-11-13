import sys,re

ofile=open(sys.argv[-1],"w")

hd='''SEQUENCE_TARGET=250,50
PRIMER_TASK=pick_detection_primers
PRIMER_PICK_LEFT_PRIMER=1
PRIMER_PICK_INTERNAL_OLIGO=0
PRIMER_PICK_RIGHT_PRIMER=1
PRIMER_OPT_SIZE=22
PRIMER_MIN_SIZE=20
PRIMER_MAX_SIZE=25
PRIMER_MAX_NS_ACCEPTED=1
PRIMER_PRODUCT_SIZE_RANGE=100-200
P3_FILE_FLAG=1
PRIMER_EXPLAIN_FLAG=1
PRIMER_NUM_RETURN=1
=
'''

with open(sys.argv[1]) as ifile:
	while(1):
		line=ifile.readline()
		if not line:break
		if ">" in line:
			mt=re.search(">(\S+)",line)
			nm=mt.group(1)
			seq=ifile.readline()
			opt="SEQUENCE_ID="+nm+"\nSEQUENCE_TEMPLATE="+seq+hd
			ofile.write(opt)
