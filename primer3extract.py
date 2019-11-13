import sys
import re


class extract(object):
    """ extract information from primer3 output to table"""
    def __init__(self,ifile,ofile):
        self.ifile = ifile.read().split("PRIMER PICKING RESULTS FOR");self.ifile.readline()
        self.ofile = ofile
    def output(self):
        for one in self.ifile:
            ones = one.split("\n")






import sys

ifile = open(sys.argv[1]).read().split("PRIMER PICKING RESULTS FOR")
ofile = open(sys.argv[2],"w")


