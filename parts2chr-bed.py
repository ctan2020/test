####################################################################
#    convert the postion of parts into chromosome position
import sys,re

ofile = open(sys.argv[2],"w")

pos={"chr1H_part1":0,"chr1H_part2":312837513,"chr2H_part1":0,"chr2H_part2":393532674,"chr3H_part1":0,"chr3H_part2":394310633,"chr4H_part1":0,"chr4H_part2":355061206,"chr5H_part1":0,"chr5H_part2":380865482,"chr6H_part1":0,"chr6H_part2":294822070,"chr7H_part1":0,"chr7H_part2":325797516,"chrUn":0}

with open (sys.argv[1]) as ifile:
	while(1):
		line = ifile.readline()
		if not line: break
		opt=""
		if not line.startswith("#"):
			lines = line.split("\t")
			ch = lines[0].split("_")[0]
			bp = pos[lines[0]] + int(lines[1])
			bp2 = pos[lines[0]] + int(lines[2])  ##
			lines[0] = ch
			lines[1] = str(bp)
			lines[2] = str(bp2)   ##
			sep="\t"
			opt = sep.join(lines)  
		else:
			opt = line	
		ofile.write(opt)
