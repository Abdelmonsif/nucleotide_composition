import os,sys,argparse
import pandas as pd
import time
from os import listdir
import numpy as np
import matplotlib.pyplot as plt

def nt_comp(SamFile, output_nt, output_p, sora_normalized, sora):
    df = pd.read_csv(SamFile, delim_whitespace=True, names=['Qname', 'flag', 'chromosome', 'start', 'MAPQ', 'CIGAR', 'RNEXT', 'PNEXT', 'TLEN', 'seq', 'QUAL', 'lol', 'a7a', 'k', 's', 'w', 'sw', 'pw', 'pow', 'jksn'], usecols=['seq'])

    df['seq10'] = df['seq'].astype(str).str[-10:]
    df['-10'] = df['seq10'].astype(str).str[0]
    df['-9'] = df['seq10'].astype(str).str[1]
    df['-8'] = df['seq10'].astype(str).str[2]
    df['-7'] = df['seq10'].astype(str).str[3]
    df['-6'] = df['seq10'].astype(str).str[4]
    df['-5'] = df['seq10'].astype(str).str[5]
    df['-4'] = df['seq10'].astype(str).str[6]
    df['-3'] = df['seq10'].astype(str).str[7]
    df['-2'] = df['seq10'].astype(str).str[8]
    df['-1'] = df['seq10'].astype(str).str[9]

    df1 = df['-10'].value_counts().reset_index()
    df2 = df1.T
    df2.columns= df2.iloc[0]
    df3 = df2[1:]
    df4 = df3.append(df['-9'].value_counts())
    df5 = df4.append(df['-8'].value_counts())
    df6 = df5.append(df['-7'].value_counts())
    df7 = df6.append(df['-6'].value_counts())
    df8 = df7.append(df['-5'].value_counts())
    df9 = df8.append(df['-4'].value_counts())
    df10 = df9.append(df['-3'].value_counts())
    df11 = df10.append(df['-2'].value_counts())
    df12 = df11.append(df['-1'].value_counts())
    final_output1 = df12.fillna(0)
    final_output = final_output1[['A', 'C', 'G', 'T']]
    final_output.to_csv(output_nt, index=False, sep='\t')
    n = final_output.sum(axis=1)
    habal = (final_output/n[0]) * 100
    habal.to_csv(output_p, index=False, sep='\t')
    colors = ["#fd3c06", "#fdaa48", "#a2cffe", "#436bad"]
    ax = habal.plot.bar(stacked=True, figsize=(20,10), color=colors)
    ax.legend(bbox_to_anchor=(1,1),prop={'size': 26})
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.xlabel('\nNucleotide position', fontsize=24)
    plt.ylabel('Percentage of Nucleotides (%)', fontsize = 24)
    fig = ax.get_figure()
    fig.savefig(sora_normalized, dpi=100)
    colors = ["#fd3c06", "#fdaa48", "#a2cffe", "#436bad"]
    ax = final_output.plot.bar(stacked=True, figsize=(20,10), color=colors)
    ax.legend(bbox_to_anchor=(1,1),prop={'size': 26})
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.xlabel('\nNucleotide position', fontsize=24)
    plt.ylabel( 'Nucleotides composition', fontsize = 24)
    fig = ax.get_figure()
    fig.savefig(sora, dpi=100)

def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-SamFile', required=True)
    parser.add_argument('-output_nt', required=True)
    parser.add_argument('-output_p', required=True)
    parser.add_argument('-sora_normalized', required=True)
    parser.add_argument('-sora', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = getArgs()
    start = time.time()
    filename = nt_comp(args.SamFile, args.output_nt, args.output_p, args.sora_normalized, args.sora)
    end = time.time()
    print ('time elapsed:' + str(end - start))
