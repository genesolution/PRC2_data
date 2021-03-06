# The code to make a table for gene 'EED'
# 
# Here we calculate all genes which mutations are statistically often lead to
# value < -0.5 with a good p-value comparing to all
# and value < 0 with a good p-value comaring to all
#
#
# The code is written by Chetverina O.A.
#
# for the research
#
# Clinical Correlations of Polycomb Repressive Complex 2 in Different Tumor Types
# Maksim Erokhin1, †, Olga Chetverina1-3, †, Balázs Győrffy 4,5 ,
# Victor V. Tatarskiy 6 , Vladic Mogila 7 , Alexander A. Shtil 6 ,
# Igor B. Roninson 8 , Jerome Moreaux 9-12 , Pavel G. Georgiev 7 ,
# Giacomo Cavalli 9* , Darya Chetverina 13* .


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from scipy.stats import chisquare

mutations = pd.read_csv( 'CCLE_mutations.csv',sep='\t')

genes = pd.read_excel('CRISPR_20Q3_PRC2.xlsx')

print(genes.head(10))

part_m=mutations[['Hugo_Symbol','Variant_Classification','DepMap_ID']]
damaged=part_m[part_m['Variant_Classification']!='Silent']
#damaged=part_m[part_m['Variant_Classification']!='Missense_Mutation']

print(damaged.head(10))

# here we calculate -
# lines number,
# number of lines < -0.5
# number of lines < 0

table = pd.DataFrame() 

EED=np.array(genes['EED'])
one_gene=genes[['EED','DepMap_ID']]

#print(one_gene.head(10))

m_g=-0.5
g_num=len(one_gene.index)
g_less=len(one_gene[one_gene['EED']<m_g].index)
g_null=len(one_gene[one_gene['EED']<0].index)

gd_less=g_num-g_less
gd_null=g_num-g_null

#print(m_g,g_num,g_less,g_null)

mut_set=set(part_m['Hugo_Symbol'])

# here we fill the table for gene 'EED'

for i in mut_set:
    dep_map_d=damaged[damaged['Hugo_Symbol']==i]

    dep_map=dep_map_d.drop_duplicates(subset=None, keep='first', inplace=False)
    deps=dep_map['DepMap_ID'].to_list()
    mut_gene=one_gene[one_gene['DepMap_ID'].isin(deps)]
    
    num= len(mut_gene.index)
    m_less=len(mut_gene[mut_gene['EED']<m_g].index)
    m_null=len(mut_gene[mut_gene['EED']<0].index)
     
    d_less=num-m_less
    d_null=num-m_null
    
    p_null=num*g_null/g_num
    dp_null=(g_num-num)*g_null/g_num

    p_less=num*g_less/g_num
    dp_less=(g_num-num)*g_less/g_num

    if m_null>0:
        x2_null=(m_null-p_null)*(m_null-p_null)/p_null+(g_null-m_null-dp_null)*(g_null-m_null-dp_null)/dp_null
    else:
        x2_null=0

    if m_less>0:
        x2_less=(m_less-p_less)*(m_less-p_less)/p_less+(g_less-m_less-dp_less)*(g_less-m_less-dp_less)/dp_less
    else:
        x2_less=0
        

    if x2_null>3.6 and m_null>p_null :
        new_row={"Mutation":i,"Rule":"<0", "Mut_num":num, "Mut<":m_null, "dMut<":g_null-m_null, "pMut<":p_null, "dpMut<":dp_null, "half X2":x2_null}
        table=table.append(new_row,ignore_index=True)

    if x2_less>3.6 and m_less>p_less:
        new_row={"Mutation":i,"Rule":"<-0.5", "Mut_num":num, "Mut<":m_less, "dMut<":g_less-m_less, "pMut<":p_less, "dpMut<":dp_less, "half X2":x2_less}
        table=table.append(new_row,ignore_index=True)
        

table['p-value']=chisquare([table["Mut<"],table["dMut<"]],[table["pMut<"],table["dpMut<"]])[1]

table = table[["Mutation", "Rule", "Mut_num","Mut<","dMut<", "pMut<","dpMut<","half X2","p-value"]]
table.to_excel("EED_0_5.xlsx")


exit()
