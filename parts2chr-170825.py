####################################################################
#    convert the postion of parts into chromosome position
import sys,re

def parts2chr_vcf(ifile,ofile):
    ofile = open(ofile,"w")
    
    header="""##contig=<ID=chr1,length=558535432>
    ##contig=<ID=chr2,length=768075024>
    ##contig=<ID=chr3,length=699711114>
    ##contig=<ID=chr4,length=647060158>
    ##contig=<ID=chr5,length=670030160>
    ##contig=<ID=chr6,length=583380513>
    ##contig=<ID=chr7,length=657224000>
    ##contig=<ID=chr8,length=249774706>
"""
    pos={"chr1H_part1":0,"chr1H_part2":312837513,"chr2H_part1":0,"chr2H_part2":393532674,"chr3H_part1":0,"chr3H_part2":394310633,"chr4H_part1":0,"chr4H_part2":355061206,"chr5H_part1":0,"chr5H_part2":380865482,"chr6H_part1":0,"chr6H_part2":294822070,"chr7H_part1":0,"chr7H_part2":325797516,"chrUn":0}
    
    with open (ifile) as ipt:
        while(1):
            line = ipt.readline()
            if not line: break
            opt=""
            if not line.startswith("#"):
                lines = line.split("\t")
                ch = lines[0].split("H_")[0]
                bp = pos[lines[0]] + int(lines[1])
                #bp2 = int(pos[lines[0]][4]) + int(lines[2])  ##
                if ch=='chrUn':
                    ch='chr8'
                lines[0] = ch
                lines[1] = str(bp)
                #lines[2] = str(bp2)   ##
                sep="\t"
                opt = sep.join(lines)
            elif line.startswith("##reference"):
                opt = line + header
            elif line.startswith("##contig"):
                opt = ""
            else:
                opt = line
            ofile.write(opt)


def parts2chr_bim(ifile,ofile):
    "convert parts positions to chr postions in barley"
    parts={"chr1H_part1":0,"chr1H_part2":312837513,"chr2H_part1":0,"chr2H_part2":393532674,"chr3H_part1":0,"chr3H_part2":394310633,"chr4H_part1":0,"chr4H_part2":355061206,"chr5H_part1":0,"chr5H_part2":380865482,"chr6H_part1":0,"chr6H_part2":294822070,"chr7H_part1":0,"chr7H_part2":325797516,"chr8":0}
    outpt=open(ofile,"w")
    with open(ifile) as inpt1:
        while(1):
            line = inpt1.readline().strip()
            if not line: break
            lines = line.split()
            if lines[0]=="chrUn":
                lines[0]="chr8"
            ch = lines[0].split("H_")[0]
            pos = int(lines[3]) + parts[lines[0]]
            lines[0],lines[3] = ch,str(pos)
            opt = "\t".join(lines)+"\n"
            outpt.write(opt)
            
def chr2parts(ifile,ofile):
    "covert chr positons to parts positions in barley"
    parts={"chr1H":312837513,"chr2H":393532674,"chr3H":394310633,"chr4H":355061206,"chr5H":380865482,"chr6H":294822070,"chr7H":325797516}
    outpt = open(ofile,"w")
    with open(ifile) as inpt1:
        while(1):
            line = inpt1.readline().strip()
            if not line:break
            lines = line.split()
            if lines[0] == "chrUn":
                pass
            elif int(lines[1]) > parts[lines[0]]:
                chr = lines[0] + "_part2"
                pos = int(lines[1]) - parts[lines[0]]
            elif int(lines[1]) <= parts[lines[0]]:
                chr = lines[0] + "_part1"
                pos =lines[1]
            lines[0:2] = chr,str(pos)
            opt = "\t".join(lines) + "\n"
            outpt.write(opt)                
            
parts2chr(sys.argv[1],sys.argv[2])
