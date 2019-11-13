import os,re,sys

ofile = open(sys.argv[3],"w")

list = {}
with open (sys.argv[1]) as ifile1:
        while(1):
                line = ifile1.readline()
                if not line:break
                lines = line.split()
#                pos = str(lines[0]) + ":" + str(lines[1]) + "-" + str(lines[2])
                list[lines[0]] = lines[1]

with open (sys.argv[2]) as ifile2:
        while(1):
                line = ifile2.readline().strip()
                if not line:break
                mt = re.search("(HORVU[0-9a-zA-Z]*\.1)\D",line)
                if mt:
                        pos = mt.group(1)
                        if pos in list.keys():
                            pos2 = line+"\t"+list[pos]+"\n"
                            ofile.write(pos2)
