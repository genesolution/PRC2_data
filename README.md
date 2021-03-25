# PRC2_data

## DepMap files for the analysis

All the initial data files could be downloaded using this link:

https://depmap.org/portal/download/ 

DepMap 20Q3 Public. 
 
DepMap (https://depmap.org/portal/) analysis of the dependency of a panel of tumor cell lines on individual genes was conducted using the CRISPR (Avana) Public 20Q3 (DepMap, Broad (2020): DepMap 20Q3 Public. figshare. Dataset doi:10.6084/m9.figshare.12931238.v1.) (33,34). 
 
The following files of the Public 20Q3 release were downloaded for the analysis:
 
 
CCLE_mutations.csv – 276.1 Mb – file contains information of mutations in cell lines. 
 
 
Achilles_gene_effect.csv – 276 Mb – file contains information of the genes Crispr knockout effect on cell lines.
 
 
The silent mutations were excluded from the analysis using the attribute ‘Variant_Classification’ in ‘CCLE_mutations.csv’ file.
 
 
## Code for the calculations  

The needed code files that are needed:
Genes_EZH2.py  - calculates all the statistics for the EZH2

It takes as input 2 files that have to be located in the same directory:

CCLE_mutations.csv
CRISPR (AVANA) Public 20Q3 PRC2 basic.xlsx

The execution is the same as for any Python program without extra parameters:
python3 Genes_EZH2.py

Same calculations for EED could be done using:
Genes_EED.py

