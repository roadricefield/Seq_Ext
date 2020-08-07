# Seq Ext

This python script extracts DNA sequence of the positions specified by BED format file from the genome.  

## Requirements:  

- Python3
- pandas
- linecache

## Usage:

```
python Seq_Ext.py [Your BED file] [Path to your directory which contains genome FASTA files] [The number of characters contained in one row of the output FASTA file, default = 50]
```

Notes:  
1. The end of the second command line argument must be "/". 
2. Your FASTA file must be separated by the chromosomes and named "chr1.fa", "chr2.fa", ... , "chrY.fa".  
3. This script prints the result to *stdout*.  
4. Sorting your input BED file by chromosomes can speed up the script.

## Example:

This repository contains the test data, `Test_regions.bed` and dummy FASTA file `chrA.fa`. You can test this script just running,  

```
$ python Seq_Ext.py Test_regions.bed ./ > res.fa
```  

The result should be following;

```
>chrA_4555-4655
ATAACTGAATTTATCAAGCAGAGTCTGAACTTCCAATCCTGTCAGAAGCC
ATCTTACTGCATCTCAGGGAATACACCAATGTACCAACTCCCTTTTTCAG

>chrA_5555-5655
CAGAGTTCATGGCAGGGAAGGAATGTTCAtggttacagtgtatcgtcagt
caggagccctgaagtttgggctggaaccagctgcaggtgacaacccaaaa

>chrA_6555-6655
gcctggttgaagtaggtgtgtcactgtgggcatgggctttaatcctcggt
gcctggaagccagtcttctagctgccttcagaacaattggtgaaaccttc
```