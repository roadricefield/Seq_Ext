import sys
import math
import linecache
import pandas as pd

#sys.argv[1]: input bed file
#sys.argv[2]: path to the directory which contains genome sequences

#The number of characters contained in each row in your genome FASTA files
fasta_width = 50

output_fasta_width = 50
if len(sys.argv) == 4: output_fasta_width = int(sys.argv[3])

if len(sys.argv) < 3:
    print("Usage: python extract_sequence.py [path to your input BED file] " 
    "[path to the directory which contains your genome FASTA files]  "
    "[The number of characters contained in each row of the output FASTA, default = 50]")

input_bed = pd.read_table(sys.argv[1], header = None)

fasta_dir = sys.argv[2]

now_chr = 'XXX'

for i in range(len(input_bed)):

    region = list(input_bed.loc[i])

    if region[0] != now_chr:
        linecache.clearcache()
        now_chr = region[0]

    start, end = region[1], region[2]
    
    start_row = math.floor(start/fasta_width) + 1
    end_row = math.floor(end/fasta_width) + 1

    S = []

    for j in range(end_row - start_row + 1):
        chr_fasta = fasta_dir + now_chr + '.fa'
        tmp = linecache.getline(chr_fasta, start_row + 1 + j)
        tmp = tmp[0:(len(tmp)-1)]
        S.append(tmp)

    Seq = "".join(S)

    extracted_Seq = Seq[start - fasta_width*(start_row-1):(len(Seq) - (fasta_width*end_row - end))]

    M = math.floor(len(extracted_Seq)/output_fasta_width)

    print(">" + region[0] + "_" + str(region[1]) + "-" + str(region[2]))
    index=0
    for _ in range(M):
        print(extracted_Seq[index:index+output_fasta_width])
        index += output_fasta_width
    if (len(extracted_Seq[index:]) > 0): print(extracted_Seq[index:])
    print("")