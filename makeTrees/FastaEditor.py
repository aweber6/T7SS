#!/usr/bin/env python

import sys
from Bio import SeqIO

## This script is used create a new FASTA file containing only the genes
## supplied in a text file (one per line) and an original FASTA file 
## from which to extract these genes from

def parse_fasta(infilename, outfilename, strain):
    records = []
    for seq_record in SeqIO.parse(infilename, "fasta"):
        if seq_record.id in strain:
            records.append(seq_record)
    SeqIO.write(records, outfilename, "fasta")

# check for correct arguments
if len(sys.argv) < 3:
    print("Usage: FastaStrainParser.py <inputfile> <outfile> <strainfile>")
    sys.exit(0)

infilename = sys.argv[1]
outfilename = sys.argv[2]
#strain = sys.argv[2:-1]
strainfile = sys.argv[3]

f = open(strainfile,"r")
strains = f.readlines()
strain = list()
for i in strains:
	clean_strain = i.replace('"', '').strip()
	print clean_strain
	strain.append(clean_strain)
print strain
parse_fasta(infilename, outfilename, strain)


