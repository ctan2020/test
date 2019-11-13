class parts(object):
    bed = dict(chr1H_part1=["chr1H",0],
              chr1H_part2=["chr1H",312837513],
              chr2H_part1=["chr2H",0],
              chr2H_part2=["chr2H",393532674],
              chr3H_part1=["chr3H",0],
              chr3H_part2=["chr3H",394310633],
              chr4H_part1=["chr4H",0],
              chr4H_part2=["chr4H",355061206],
              chr5H_part1=["chr5H",0],
              chr5H_part2=["chr5H",380865482],
              chr6H_part1=["chr6H",0],
              chr6H_part2=["chr6H",294822070],
              chr7H_part1=["chr7H",0],
              chr7H_part2=["chr7H",325797516],
              chrUn=["chrUn",0])
    def __init__(self,chr,pos):
        self.chr = chr
        self.pos = pos
    def position(self):
        chr2 = parts.bed[self.chr][0]
        pos2 = int(parts.bed[self.chr][1])+self.pos
        return([chr2,pos2])
