import sys,os

def _gene_in_bed(beds,ofile):
    """"
    find genes in regions
    """
    genes=open("/home/ctan/data/ref/Hordeum_vulgare/barley/anno/hc_genes_info.tab").readlines()
    list=[]
    for line in beds:
            list.append(line.split())
    for gene in genes:
            lines=gene.split(",")
            for i in range(0,len(list)):
                    if list[i][0] == lines[1] and int(list[i][1])<=int(lines[2]) and int(list[i][2]) >= int(lines[3]):
                        opt = "\t".join([list[i][0],list[i][1],list[i][2]])+"\t"+"\t".join(lines)
                        ofile.write(opt)

ifile=open(sys.argv[1]).readlines()

ofile = open(sys.argv[2],"w")

_gene_in_bed(ifile,ofile)

