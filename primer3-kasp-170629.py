from primer3 import bindings
import sys
import pysam
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

ifile = open(sys.argv[1]).readlines()
ofile = open(sys.argv[2], "w")

hd = "\t".join(["#primer_id",
                "primer_seq",
                "product_size",
                "start_length",
                "Tm",
                "GC_percent"
                ]) + "\n"
ofile.write(hd)

ref = pysam.Fastafile("/home/ctan/data/ref/Hordeum_vulgare/barley/blast/160404_barley_pseudomolecules_masked.fasta")
tails = ["GAAGGTGACCAAGTTCATGCT", "GAAGGTCGGAGTCAACGGATT"]

for one in ifile:
    if not one.startswith("#"):
        ones = one.split()
        seq_id = "_".join([ones[0], ones[1], ones[3], ones[4]])
        seq = ref.fetch(ones[0], int(ones[1]) - 250, int(ones[1]) + 300)
        tag = ref.fetch(ones[0], int(ones[1]) - 25, int(ones[1]) - 1) + "[" + "/".join(ones[3:5]) + "]" + ref.fetch(
            ones[0], int(ones[1]), int(ones[1]) + 25)
        alt = Seq(ones[4], generic_dna)
        primer = bindings.designPrimers(
            {
                'SEQUENCE_ID': seq_id,
                'SEQUENCE_TEMPLATE': seq,
                'SEQUENCE_FORCE_LEFT_END': 249
            },
            {'PRIMER_OPT_SIZE': 22, 'PRIMER_NUM_RETURN': 1, 'PRIMER_PICK_INTERNAL_OLIGO': 0,
             'PRIMER_INTERNAL_MAX_SELF_END': 8, 'PRIMER_MIN_SIZE': 18, 'PRIMER_MAX_SIZE': 25, 'PRIMER_OPT_TM': 60.0,
             'PRIMER_MIN_TM': 57.0, 'PRIMER_MAX_TM': 63.0, 'PRIMER_MIN_GC': 20.0, 'PRIMER_MAX_GC': 80.0,
             'PRIMER_MAX_POLY_X': 100, 'PRIMER_INTERNAL_MAX_POLY_X': 100, 'PRIMER_SALT_MONOVALENT': 50.0,
             'PRIMER_DNA_CONC': 50.0, 'PRIMER_MAX_NS_ACCEPTED': 0, 'PRIMER_MAX_SELF_ANY': 12, 'PRIMER_MAX_SELF_END': 8,
             'PRIMER_PAIR_MAX_COMPL_ANY': 12, 'PRIMER_PAIR_MAX_COMPL_END': 8,'PRIMER_PRODUCT_SIZE_RANGE':[[100,300]],
             })
        primer2 = bindings.designPrimers(
            {
                'SEQUENCE_ID': seq_id,
                'SEQUENCE_TEMPLATE': seq,
                'SEQUENCE_FORCE_RIGHT_END': 249
            },
            {'PRIMER_OPT_SIZE': 22, 'PRIMER_NUM_RETURN': 1, 'PRIMER_PICK_INTERNAL_OLIGO': 0,
             'PRIMER_INTERNAL_MAX_SELF_END': 8, 'PRIMER_MIN_SIZE': 18, 'PRIMER_MAX_SIZE': 25, 'PRIMER_OPT_TM': 60.0,
             'PRIMER_MIN_TM': 57.0, 'PRIMER_MAX_TM': 63.0, 'PRIMER_MIN_GC': 20.0, 'PRIMER_MAX_GC': 80.0,
             'PRIMER_MAX_POLY_X': 100, 'PRIMER_INTERNAL_MAX_POLY_X': 100, 'PRIMER_SALT_MONOVALENT': 50.0,
             'PRIMER_DNA_CONC': 50.0, 'PRIMER_MAX_NS_ACCEPTED': 0, 'PRIMER_MAX_SELF_ANY': 12, 'PRIMER_MAX_SELF_END': 8,
             'PRIMER_PAIR_MAX_COMPL_ANY': 12, 'PRIMER_PAIR_MAX_COMPL_END': 8,'PRIMER_PRODUCT_SIZE_RANGE':[[100,300]]
             }
        )
        if primer['PRIMER_PAIR_NUM_RETURNED'] >= 1:
            ofile.write("\t".join(
                ["#" + seq_id, tag, primer['PRIMER_LEFT_0_SEQUENCE'], primer['PRIMER_RIGHT_0_SEQUENCE']]) + "\n")
            opt1 = "\t".join([seq_id + "_1F",
                              tails[0] + primer['PRIMER_LEFT_0_SEQUENCE'],
                              str(primer['PRIMER_PAIR_0_PRODUCT_SIZE']),
                              str(primer['PRIMER_LEFT_0']),
                              str(int(primer['PRIMER_LEFT_0_TM'])),
                              str(int(primer['PRIMER_LEFT_0_GC_PERCENT']))
                              ])
            ofile.write(opt1 + "\n")
            alle2f = primer['PRIMER_LEFT_0_SEQUENCE'][:-1] + ones[4]
            opt1b = "\t".join([seq_id + "_2F",
                               tails[1] + alle2f,
                               str(primer['PRIMER_PAIR_0_PRODUCT_SIZE']),
                               str(primer['PRIMER_LEFT_0']),
                               str(int(primer['PRIMER_LEFT_0_TM'])),
                               str(int(primer['PRIMER_LEFT_0_GC_PERCENT']))
                               ])
            ofile.write(opt1b + "\n")
            opt2 = "\t".join([seq_id + "_R",
                              primer['PRIMER_RIGHT_0_SEQUENCE'],
                              str(primer['PRIMER_PAIR_0_PRODUCT_SIZE']),
                              str(primer['PRIMER_RIGHT_0']),
                              str(int(primer['PRIMER_RIGHT_0_TM'])),
                              str(int(primer['PRIMER_RIGHT_0_GC_PERCENT']))
                              ])
            ofile.write(opt2 + "\n")
        elif primer2['PRIMER_PAIR_NUM_RETURNED'] >= 1:
            ofile.write("\t".join(
                ["#" + seq_id, tag, primer2['PRIMER_LEFT_0_SEQUENCE'], primer2['PRIMER_RIGHT_0_SEQUENCE']]) + "\n")
            opt1 = "\t".join([seq_id + "_F",
                              primer2['PRIMER_LEFT_0_SEQUENCE'],
                              str(primer2['PRIMER_PAIR_0_PRODUCT_SIZE']),
                              str(primer2['PRIMER_LEFT_0']),
                              str(int(primer2['PRIMER_LEFT_0_TM'])),
                              str(int(primer2['PRIMER_LEFT_0_GC_PERCENT']))
                              ])
            ofile.write(opt1 + "\t" + tag + "\n")
            opt2 = "\t".join([seq_id + "_1R",
                              tails[0] + primer2['PRIMER_RIGHT_0_SEQUENCE'],
                              str(primer2['PRIMER_PAIR_0_PRODUCT_SIZE']),
                              str(primer2['PRIMER_RIGHT_0']),
                              str(int(primer2['PRIMER_RIGHT_0_TM'])),
                              str(int(primer2['PRIMER_RIGHT_0_GC_PERCENT']))
                              ])
            ofile.write(opt2 + "\n")
            alle2r = primer2['PRIMER_RIGHT_0_SEQUENCE'][:-1] + alt.complement()._data
            opt2b = "\t".join([seq_id + "_2R",
                               tails[1] + alle2r,
                               str(primer2['PRIMER_PAIR_0_PRODUCT_SIZE']),
                               str(primer2['PRIMER_RIGHT_0']),
                               str(int(primer2['PRIMER_RIGHT_0_TM'])),
                               str(int(primer2['PRIMER_RIGHT_0_GC_PERCENT']))
                               ])
            ofile.write(opt2b + "\n")
