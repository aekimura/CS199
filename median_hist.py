#!/usr/bin/env python3

import sys
import statistics
import pandas
import seaborn
import matplotlib.pyplot as plt

def median_hist (file_path: str) -> int:
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
        seaborn.distplot(values_table['Median'], hist = True, kde = False, rug = False)
        plt.title('Median Probability Correct Values for mytestfile.fastq')
        plt.xlabel('Median Probability Values')
        plt.ylabel('Counts')
        plt.show()

if __name__ == '__main__':
        median_hist(sys.argv[1])
