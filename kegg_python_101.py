#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import pandas as pd
import matplotlib as plt
import math

# INPUT GENOME #
#run genes (identified by prokka) through ghostkoala
kegg_file = pd.read_csv('case2_kegg_ko.tsv', names = ['gene', 'K_no'], sep = '\t').set_index('gene').dropna()

input_list = kegg_file.K_no.tolist() # read in kegg gene identifier numbers as list

# KEGG GENES #
# genes interested in - list form
# definition from kegg module entry

modules_oi = {}
modules_oi["calvin_cycle"] = "K00855 (K01601-K01602) K00927 (K05298,K00150,K00134) (K01623,K01624) (K03841,K02446,K11532,K01086) K00615 (K01623,K01624) (K01100,K11532,K01086) K00615 (K01807,K01808)"
modules_oi["methanol_to_methane"] = "K14080+K04480+K14081 K00399+K00401+K00402 (K22480+K22481+K22482,K03388+K03389+K03390,K08264+K08265,K03388+K03389+K03390+K14127+(K14126+K14128,K22516+K00125))"
modules_oi["acetate_to_methane"] = "(K00925 (K00625,K13788),K01895) (K00193+K00197+K00194) (K00577+K00578+K00579+K00580+K00581-K00582-K00583+K00584) (K00399+K00401+K00402) (K22480+K22481+K22482,K03388+K03389+K03390,K08264+K08265,K03388+K03389+K03390+K14127+(K14126+K14128,K22516+K00125))"
modules_oi["methalamine_to_methane"] = "K14082 ((K16177-K16176),(K16179-K16178),(K14084-K14083)) K00399+K00401+K00402 (K22480+K22481+K22482,K03388+K03389+K03390,K08264+K08265,K03388+K03389+K03390+K14127+(K14126+K14128,K22516+K00125))"

# PATHWAY #
for module in modules_oi:
    genes_oi = modules_oi[module].strip("()")
    genes_oi = re.split('\W+', genes_oi)
    genes_oi= set(genes_oi)
    gene_count = {} #create an empty dictionary
    for gene in genes_oi: #for each item in input_list
        if gene in input_list: #if the item is in genes of interest
            if gene in gene_count: # if the gene is already a key in the dictionary add one to the value
                gene_count[gene] +=1
            else: # if gene is not already a key in the dictionary set value to 1
                gene_count[gene] = 1
        else:
            gene_count[gene] = 0
    print(module + " ", gene_count)
