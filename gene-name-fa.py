
import os,re,sys

ofile = open(sys.argv[3],"w")

list = {}
with open (sys.argv[1]) as ifile1:
        while(1):
                line = ifile1.readline()
                if not line:break
                lines = line.split()
                pos = str(lines[0]) + ":" + str(lines[1]) + "-" + str(lines[2])
                list[pos] = lines[3]

with open (sys.argv[2]) as ifile2:
        while(1):
                line = ifile2.readline()
                if not line:break
                mt = re.search(">([chrHUn\:\-0-9]*)$",line)
                if mt:
                        pos = mt.group(1)
                        pos2 = ">" + list[pos] + " genomic|" + pos + "\n"
                        ofile.write(pos2)
                else:
                        ofile.write(line)
