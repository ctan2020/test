
class vcf_record(object):
    #parse each record in vcf files
    def __init__(self,line):
        self.line = line
        self.lines = line.split()
        self.INDEL = len(self.lines[4].split(",")[0]) - len(self.lines[3])
        self.lines[2] = str(self.INDEL)
        self.fmt = self.lines[8].split(":")
        self.GT = []
        self.AD0 = []
        self.AD1 = []
        for i in range(9,len(self.lines)):
            genotype = self.lines[i].split(":")[0]
            self.GT.append(genotype)
            if genotype == "./.":
                self.AD0.append(0)
                self.AD1.append(0)
            else:
                self.AD0.append(int(self.lines[i].split(":")[self.fmt.index("AD")].split(",")[0]))
                self.AD1.append(int(self.lines[i].split(":")[self.fmt.index("AD")].split(",")[1]))
        self.HOMO = self.GT.count("0/0")
        self.ALT = self.GT.count("1/1")
        self.HET = self.GT.count("0/1")
        self.OPT = self.lines[0:4] + [str(self.HOMO),self.lines[4],str(self.ALT)]
    def filter(self):
        rt = 0
        for i in range(0,len(self.GT)):
            if self.GT[i] == "1/1" and self.AD1[i] >= 5:
                rt = 1
        return rt
    def diff(self, id1, id2):
        if self.GT[id1] == "1/1" and self.GT[id2] == "0/0":
            return 1
        elif self.GT[id2] == "1/1" and self.GT[id1] == "0/0":
            return 1
        else:
            return 0

class samvcf(object):
    def __init__(self,one):
        self.one = one
        self.ref = 0
        self.alt = 0
        self.het = 0
        self.indel = len(self.one.alleles[1]) - len(self.one.alleles[0])
        for smp in self.one.samples.keys():
            if self.one.samples[smp]['GT'][0]:
                if sum(self.one.samples[smp]['GT']) == 0:
                    self.ref = self.ref + 1
                elif sum(self.one.samples[smp]['GT']) == 1:
                    self.het = self.het +1
                elif sum(self.one.samples[smp]['GT']) == 2:
                    self.alt = self.alt +1
        self.opt = [self.one.chrom,str(self.one.pos),str(self.indel),self.one.ref,self.one.alts[0]] + [",".join([str(self.ref),str(self.het),str(self.alt)])]
    def diff(self,pt1,pt2):
        if self.one.samples[pt1]['GT'][0] and self.one.samples[pt2]['GT'][0]:
            if sum(self.one.samples[pt1]['GT']) != sum(self.one.samples[pt2]['GT']):
                return 1
            else:
                return 0
    def diff_repeat(self,smps):
        present = 1
        for one in smps:
            if self.one.samples[one]['GT'][0] is None:
                present = 0
        if present:
            if sum(self.one.samples[smps[0]]['GT']) == 0 and sum(self.one.samples[smps[1]]['GT']) == 0 and sum(self.one.samples[smps[2]]['GT']) == 2 and sum(self.one.samples[smps[3]]['GT']) == 2:
                return 1
            elif sum(self.one.samples[smps[0]]['GT']) == 2 and sum(self.one.samples[smps[1]]['GT']) == 2 and sum(self.one.samples[smps[2]]['GT']) == 0 and sum(self.one.samples[smps[3]]['GT']) == 0:
                return 1
    def diff_group(self,grp1,grp2):
        num10 = 0
        num11 = 0
        num12 = 0
        num20 = 0
        num21 = 0
        num22 = 0
        rt = 0
        for smp in grp1:
            if self.one.samples[smp]['GT'][0] is not None:
                if sum(self.one.samples[smp]['GT']) == 0:
                    num10 = num10 + 1
                elif sum(self.one.samples[smp]['GT']) == 1:
                    num11 = num11 + 1
                elif sum(self.one.samples[smp]['GT']) == 2:
                    num12 = num12 + 1
        for smp in grp2:
            if self.one.samples[smp]['GT'][0] is not None:
                if sum(self.one.samples[smp]['GT']) == 0:
                    num20 = num20 + 1
                elif sum(self.one.samples[smp]['GT']) == 1:
                    num21 = num21 + 1
                elif sum(self.one.samples[smp]['GT']) == 2:
                    num22 = num22 + 1
        if num11 == 0 and num21 == 0:
            if num10 > 0 and num12 == 0 and num20 == 0 and num22 > 0:
                rt = 1
            elif num10 == 0 and num12 >0 and num20 >0 and num22 == 0:
                rt = 1
        if rt == 1:
            gt_opt = []
            for smp in grp1 + grp2:
                if self.one.samples[smp]['GT'][0] is None:
                    gt_opt = gt_opt + ["N","0,0"]
                elif self.one.samples[smp]['GT'][0] is not None:
                    gt_opt = gt_opt + [str(sum(self.one.samples[smp]['GT']))]
            return gt_opt
    def extract(self,grp):
        num10 = 0
        num11 = 0
        num12 = 0
        for smp in grp:
            if self.one.samples[smp]['GT'][0] is not None:
                if sum(self.one.samples[smp]['GT']) == 0:
                    num10 = num10 + 1
                elif sum(self.one.samples[smp]['GT']) == 1:
                    num11 = num11 + 1
                elif sum(self.one.samples[smp]['GT']) == 2:
                    num12 = num12 + 1
        if num12 > 0 :
            gt_opt = []
            for smp in grp:
                if self.one.samples[smp]['GT'][0] is None:
                    gt_opt = gt_opt + ["N", "0,0"]
                elif self.one.samples[smp]['GT'][0] is not None:
                    gt_opt = gt_opt + [str(sum(self.one.samples[smp]['GT'])),
                                       ",".join(list(map(str, self.one.samples[smp]['AD'])))]
            return gt_opt



