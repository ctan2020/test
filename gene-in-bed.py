import sys,os,re

def _gene_pos(genes,ofile):
    """
    get gene position
    """
    ifile1=open("/ctan02/ref/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos").readlines()

    dict_genes={}
    for gene in genes:
        dict_genes[gene.split()[0]]=1

    for line in ifile1:
        lines=line.split()
        if lines[3] in dict_genes:
            opt = "\t".join(lines[0:4])+"\n"
            ofile.write(opt)

def _gene_fun(genes,ofile):
        """
        get gene position
        """
        ifile1=open("/ctan02/ref/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos.fun").readlines()

        dict_genes={}
        for gene in genes:
            gene=gene.trip()
            dict_genes[gene.split()[0]]=gene

        for line in ifile1:
                lines=line.split()
                if lines[3] in dict_genes:
                    opt=dict_genes[lines[3]] + "\t|\t"+line
                    ofile.write(opt)


def _gene_overlap(genes1,genes2,ofile):
    """
    gene overlap
    """
    dict_gene={}
    for gene in genes1:
        dict_gene[gene.split()[0]]=1
    for gene in genes2:
        if gene.split()[0] in dict_gene:
            ofile.write(gene)

def _pos_in_gene(pos,ofile):
    """
    anchor position in genes
    """
    genes=open("/ctan02/ref/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos").readlines()
    list=[]
    for line in pos:
        list.append(line.split())
    for gene in genes:
        lines=gene.split()
        for i in range(0,len(list)):
                        if list[i][0] == lines[0] and int(list[i][1])>=int(lines[1]) and int(list[i][1]) <= int(lines[2]):
                                ofile.write(gene)
def _gene_in_bed(beds):
    """"
    find genes in regions
    """
        genes=open("~/data/ref/Hordeum_vulgare/barley/anno/Hv_IBSC_PGSB_r1_HighConf.pos.fun").readlines()
        list=[]
        for line in beds:
                list.append(line.split())
        for gene in genes:
                lines=gene.split()
                for i in range(0,len(list)):
                        if list[i][0] == lines[0] and int(list[i][1])<=int(lines[1]) and int(list[i][2]) >= int(lines[2]):
                opt = "\t".joint([list[i][0],list[i][1],list[i][2]])+"\t"+"\t".joint(lines)
                                ofile.write(opt)


ifile=open(sys.argv[1]).readlines()

#ifile2=open(sys.argv[2]).readlines()

ofile = open(sys.argv[2],"w")

_gene_in_bed(ifile,ofile)

#_gene_fun(ifile1,ofile)

#_gene_pos(ifile1,ofile)

#_gene_overlap(ifile1,ifile2,ofile)
