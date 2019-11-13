##################################################
##   python get-chr-pos-150928.py ../../../dataset/130905_MxB_iSelect+OWB_GBS_maps_combined_anchoring.tsv.length.chr E2vsE7.diff E2vsE7.dir
import sys,re

ofile=open(sys.argv[3],"w")

list={}
with open(sys.argv[1]) as ifile1:
	while(1):
		line = ifile1.readline().strip()
		if not line:break
		if not line.startswith("#"):
			lines=line.split()
			list[lines[0]]=lines
			
with open(sys.argv[2]) as ifile2:
	while(1):
		line = ifile2.readline().strip()
		if not line: break
		if not line.startswith("#"):
			lines = line.split()
			if lines[0] in list.keys():
				pos1 = int(list[lines[0]][5]) + int(lines[1]) - 1
				pos2 = int(list[lines[0]][5]) + int(lines[2]) - 1
				opt = list[lines[0]][4] + "\t" + str(pos1) + "\t" + str(pos2) + "\t" + lines[3] + "\n"
				ofile.write(opt)
