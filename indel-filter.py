import sys,os

ofile=open(sys.argv[2],"w")
with open (sys.argv[1]) as ifile:
	while(1):
		line=ifile.readline()
		if not line:break
		lines=line.split("\t")
		lg=len(lines[2])-len(lines[3].split(",")[0])
		if abs(lg)>3:
			opt="\t".join([str(lg)]+lines)
			opt2=opt.replace("/","|")
			ofile.write(opt2)
