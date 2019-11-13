import sys,re,csv

# python extract-SnpTag-180914.py SNP-list180914.txt snp_data.txt SNP-list180914.fa
ofile=open(sys.argv[3],"w")

list={}
with open(sys.argv[1]) as ifile:
	while(1):
		line=ifile.readline()
		if not line:break
		lines=line.split()
		list[lines[0]]=1
#		idx = str(lines[0]) + "|" + str(lines[1])  #
#		list[idx] = 1

ifile2 = csv.reader(open(sys.argv[2]))

for row in ifile2:
	rows=row[0].split()
	if rows[0] in list.keys():
		mt = re.search("(\dH):(\d+)",rows[1])
		opt = ">" + "".join([mt.group(1),str(mt.group(2)).zfill(9)]) + "\t|" + rows[0] + "\n" + rows[2] + "\n"
		ofile.write(opt)
