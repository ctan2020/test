
import os,sys
def fa2tag(ifile1,ifile2):
    ifile=open(ifile1).readlines()
    ofile=open(ifile2,"w")
    for one in ifile:
        ones=one.split("\t")
        tag="["+ones[3]+"/"+ones[4]+"]"
        opt=">"+ones[2]+"\n"+ones[5][149:249]+tag+ones[5][250:350]+"\n"
        ofile.write(opt)


def allele2kasp(ifile1,ifile2):
    ifile=open(ifile1,"r")
    ofile = open(ifile2, "w")
    adr = ["GAAGGTGACCAAGTTCATGCT", "GAAGGTCGGAGTCAACGGATT"]
    ifiles = ifile.read().split("AS Primer Picking Result for")
    for one in ifiles:
        if "Oligo 1" in one:
            snp = re.search("(\dH\d*)\s", one).group(1)
            wtp = re.search("Wildtype \w+ Primer 5': ([ATCG]*)\s", one).group(1)
            mtp = re.search("Mutant \w+ Primer 5': ([ATCG]*)\s", one).group(1)
            ctp = re.search("Common \w+ Primer 5': ([ATCG]*)\s", one).group(1)
            ofile.write("\t".join([snp + "_FAM", adr[0] + wtp, "\n"]))
            ofile.write("\t".join([snp + "_VIC", adr[1] + mtp, "\n"]))
            ofile.write("\t".join([snp + "_C", ctp, "\n"]))

fa2tag(sys.argv[1],sys.argv[2])
