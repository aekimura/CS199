#!/usr/bin/env python3

import sys
import statistics
import pandas
import seaborn as sns
import matplotlib.pyplot as plt

def mean_median_scatter (file_path: str) -> int:
        my_file = None
        line_count = 0
        allquallist = []
        try:
                my_file = open(file_path, 'r')
                for line in my_file:
                        myquallist = []
                        statslist = []
                        line_count += 1
                        if line_count%4 == 0:
                                for char in line.strip():
                                        myquallist.append(1-(10.0**(-(ord(char)-33)/10.0)))
                                mean = (sum(myquallist)/len(myquallist))
                                median = statistics.median(myquallist)
                                list_min = min(myquallist)
                                list_max = max(myquallist)
                                statslist = [mean, median, list_min, list_max]
                                allquallist.append(statslist)
        finally:
                if my_file != None:
                        my_file.close()
        values_table = pandas.DataFrame(allquallist)
        values_table.columns = ['Mean', 'Median', 'Min', 'Max']
        pandas.options.display.precision = 16
        sns.lmplot('Mean', 'Median', values_table, fit_reg = False,  scatter_kws={"s": 25})
        plt.title('Median vs Mean Probability Correct for mytestfile.fastq')
        plt.xlabel('Mean')
        plt.ylabel('Median')
        plt.show()


if __name__ == '__main__':
        mean_median_scatter(sys.argv[1])

