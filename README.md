# Seq Ext

This python script extracts DNA sequences of the positions specified by BED file from the genome, and output the sequences in FASTA format.  

## Requirements:  

- Python3
- pandas
- linecache

## Usage:

```
python Seq_Ext.py [Your BED file] \
[Path to your directory which contains genome FASTA files] \
[The number of characters contained in each row of the output, default = 50]
```

Notes:  
1. The end of the second command line argument must be "/". 
2. Your genome FASTA files must be separated by the chromosomes and named <br>"chr1.fa", "chr2.fa", ... , "chrY.fa".  
3. This script prints the result to *stdout*.  
4. Sorting your input BED file by chromosomes can speed up the script.  
5. If the number of characters in each row of your genome FASTA files is not 50, <br>please set the correct number to the variable `fasta_width` in `Seq_Ext.py`.   

## Example:

This repository contains the test data, a BED file `Test_regions.bed` and a dummy genome FASTA file `chrA.fa` in the directory `Test_data`. You can test this script just running,  

```
$ python Seq_Ext.py ./Test_data/Test_regions.bed ./Test_data/ > res.fa
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