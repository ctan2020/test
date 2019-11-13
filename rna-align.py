
import os,sys,re

ref="/scratch/pawsey0114/ctan/ref-150901/bowtie2/Hv_IBSC_PGSB_v2_Dez2015_final_transcripts.fa"

with open(sys.argv[1]) as ifile:
	while (1):
		line = ifile.readline().strip()
		if not line:break
		mt = re.search("(..\/CleanData\/[^\/]+)\/(\S*)_1.fq.gz",line)
		dr = mt.group(1)
		sm = mt.group(2)
		fq1= dr + "/" + sm + "_1.fq.gz"
		fq2 = dr + "/" + sm + "_2.fq.gz"
		opt = "#!/bin/sh -l \nmodule load samtools \nmodule load bowtie2\n\n"
		
		ofile = open(sm + "-align.sh", "w")
		if os.path.exists(fq1) and os.path.exists(fq2):
			opt = opt + "bowtie2 --phred64 -x " + ref +" -1 " + fq1 + " -2 " + fq2 + " -S ../Alignment/" + sm + ".sam \n"
			opt = opt + "samtools view -bS ../Alignment/" + sm + ".sam > ../Alignment/" + sm + ".bam \n"
			opt = opt + "samtools sort ../Alignment/" + sm + ".bam ../Alignment/" + sm + ".sorted \n"
			ofile.write(opt)
