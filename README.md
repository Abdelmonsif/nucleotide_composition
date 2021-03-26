A python script to identify the nucleotide composition of the 3' end of a sam file

SAM file is the output of STAR alignment



Python requirements:

python3

packages:

pandas, numpy matplotlib, os, sys, time

Run:
python nt_comp.py -SamFile ./a7a1.sam -output_nt a7a1_nt_comp.tab -output_p a7a1_nt_comp_p.tab -sora_normalized a7a1_normalized.png -sora a7a1.png

