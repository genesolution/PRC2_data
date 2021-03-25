# PRC2_data

## DepMap files for the analysis

All the initial data files could be downloaded using this link:

https://depmap.org/portal/download/ 

The files are located at:

"https://figshare.com/articles/dataset/public_20q3/12931238/1" 
 

DepMap (https://depmap.org/portal/) analysis of the dependency of a panel of tumor cell lines on individual genes was conducted using the CRISPR (Avana) Public 20Q3 (DepMap, Broad (2020): DepMap 20Q3 Public. figshare. Dataset doi:10.6084/m9.figshare.12931238.v1.) (33,34). 
 
 
 
The following files of the Public 20Q3 release were downloaded for the analysis:
 
* CCLE_mutations.csv – 276.1 Mb – the file contains information of mutations in cell lines. 
 
* Achilles_gene_effect.csv – 276 Mb – the file contains information of the genes Crispr knockout effect on cell lines.
 
 
The silent mutations were excluded from the analysis using the attribute ‘Variant_Classification’ in ‘CCLE_mutations.csv’ file.
 
##  CRISPR_20Q3_PRC2.xlsx 
 
This table was received by taking and renaming the needed columns for the PRC2 research from the file:

Achilles_gene_effect.csv 

Due to quite small size, we have added it to this repository:

CRISPR_20Q3_PRC2.xlsx 


## Code for the calculations  

The executable code files:
<p> Genes_EZH2.py  - calculates all the statistics for the EZH2
<p> Genes_EED.py  - same for EED
<p> Genes_EED.py  - same for SUZ12
 
All take as input 2 files that have to be located in the same directory:

* CCLE_mutations.csv
* CRISPR_20Q3_PRC2.xlsx

The execution line is the same as for any Python program without extra parameters:

'python3 Genes_EZH2.py'



