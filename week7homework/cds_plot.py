#!/usr/bin/env python3

import sys
import seaborn
import matplotlib.pyplot as plt

def file_to_data (file_path: 'Path') -> list:
        my_file = None
        data = []
        try:
                my_file = open(file_path, 'r')
                for line in my_file:
                        data.append(int(line))
        finally:
                if my_file != None:
                        my_file.close()
        return data

def plot(data1: 'iso1 contigs', data2: 'dmel contigs') -> 'plot':
        cdf_plot = seaborn.distplot(data1,  kde_kws = dict(cumulative=True), bins = 1000, label = 'iso1 assembly')
        seaborn.distplot(data2, kde_kws = dict(cumulative=True),  bins = 1000, label = 'dmel assembly')
        cdf_plot.set_title('CDF Plot: D. mel Reference vs. Iso1 Nanopore Genome Assembly')
        cdf_plot.set_ylabel('Proportion of Assembly')
        cdf_plot.set_xlabel('Contig Length')
        plt.legend()
        plt.show()

if __name__ == '__main__':
        iso1_data = file_to_data(sys.argv[1])
        dmel_data = file_to_data(sys.argv[2])
        plot(iso1_data, dmel_data)

