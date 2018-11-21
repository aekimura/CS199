#!/usr/bin/env python3

import sys
import seaborn
import matplotlib.pyplot as plt

def get_contigs (file_path: 'Path') -> list:
	my_file = None
	line_count = 0
	headers = []
	text = []
	result = []
	try:
		my_file = open(file_path, 'r')
		for line in my_file:
			if line.startswith('>'):
				headers.append(line_count)
			text.append(line)
			line_count += 1
		for h in range(len(headers)):
			if headers[h] < headers[-1]:
				contig_len = 0
				for line in text[((headers[h]) + 1):headers[h + 1]]:
					contig_len += len(line)
				result.append(contig_len)
			if headers[h] == headers[-1]:
				contig_len = 0
				for line in text[((headers[h]) + 1):]:
					contig_len += len(line)
				result.append(contig_len)
	finally:
		if my_file != None:
			my_file.close()
	return result

def hist_contigs(contigs: list) -> 'graph':
	contig_600000 = []
	other_contigs = []
	for c in contigs:
		if c < 600000:
			contig_600000.append(c)
		else:
			other_contigs.append(c)
	seaborn.distplot(contig_600000, bins = 20, kde = False, norm_hist = False)
	plt.title('Distribution of D. melanogaster Iso1 read lengths < 600,000 bp')
	plt.xlabel('Read lengths')
	plt.ylabel('Counts')
	plt.show()
	seaborn.distplot(other_contigs, bins = 20, kde = False, norm_hist = False)
	plt.title('Distribution of D. melanogaster Iso1 read lengths >= 600,000 bp')
	plt.xlabel('Read lengths')
	plt.ylabel('Counts')
	plt.show()

def plot_cdf(lengths: list) -> 'plot':
	cdf_plot = seaborn.distplot(lengths,  kde_kws = dict(cumulative=True), bins = 1000, label = 'Flybase')
	cdf_plot.set_title('CDF Plot')
	cdf_plot.set_ylabel('Proportion of Assembly')
	cdf_plot.set_xlabel('Contig Length')
	plt.show()

if __name__ == '__main__':
	contig_lens = (get_contigs(sys.argv[1]))
	hist_contigs(contig_lens)
	plot_cdf(contig_lens)
