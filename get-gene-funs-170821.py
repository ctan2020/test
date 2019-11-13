
import csv
import sys

ifile1 = open("/home/ctan/data/ref/Hordeum_vulgare/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos.fun").readlines()

fun = {}
for one in ifile1:
	ones = one.split("\t")
	fun[ones[5]]=ones[7:10]

ifile2 = csv.reader(open(sys.argv[1]))
ofile1=csv.writer(open(sys.argv[2],"w"), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
for row in ifile2:
	if row[0] in fun.keys():
		opt = row + fun[row[0]]
		ofile1.writerow(opt)
	else:
		opt = row + ["None","None","None"]
		ofile1.writerow(opt)
