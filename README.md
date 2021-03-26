A python script to identify the nucleotide composition of the 3' end of a sam file

SAM file is the output of STAR alignment



Python requirements:

python3

packages:

pandas, numpy matplotlib, os, sys, time

Run:
python nt_comp.py -SamFile ./test_genomic.sam -output_nt test_nt_comp.tab -output_p test_nt_comp_p.tab -sora_normalized test_normalized.png -sora test.png

