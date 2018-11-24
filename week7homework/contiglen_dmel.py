#!/usr/bin/env python3

import sys
import seaborn
import matplotlib.pyplot as plt


def remove_n (file_path: 'Path') -> list:
	my_file = None
	characters = []
	break_position = []
	result = []
	try:
		my_file = open(file_path, 'r')
		for line in my_file:
			len_line = len(line)
			if line.startswith('>'):
				characters.append('|')
			else:
				n_position = []
				for char in range(len(line)):
					if line[char] == 'N':
						n_position.append(char)
				if len(n_position) == 0:
					characters.append(len(line))
				else:
					start = []
					end = []
					for position in n_position:
						if (position - 1) not in n_position:
							start.append(position)
						if (position + 1) not in n_position:
							end.append(position)
					if end == []:
						print(line)
					if len(start) == 1:
						if start[0] == 0:
							if end[0] == len_line:
								characters.append('|')
					else:
						characters.append(len(line[:start[0]]))
						for s_value in range(len(start)):
							if s > 0:
								characters.append('|')
								characters.append(len(line[end[s -1]:start[s]]))
						characters.append('|')
						characters.append(len(line[end[-1]:]))
		for item in range(len(characters)):
			if characters[item] == '|':
				break_position.append(item)
		b_start = []
		b_end = []
		for position in break_position:
			if (position - 1) not in break_position:
				b_start.append(position)
			if (position + 1) not in break_position:
				b_end.append(position)
		first_contig_len = 0
		for length in characters[1:b_start[1]]:
			first_contig_len += int(length)
		result.append(first_contig_len)
		for s_value in range(len(b_start)):
			if s_value > 0:
				contig_len = 0
				for length in characters[(b_end[s_value - 1] + 1):b_start[s_value]]:
					contig_len += int(length)
				result.append(contig_len)
		final_contig_len = 0
		for length in characters[(b_end[-1] + 1):]:
			final_contig_len += int(length)
		result.append(final_contig_len)
	finally:
		if my_file != None:
			my_file.close()
	return result


def plot(lengths: list) -> 'plot':
	cdf_plot = seaborn.distplot(lengths,  kde_kws = dict(cumulative=True), bins = 1000, label = 'Flybase')
	cdf_plot.set_title('CDF Plot')
	cdf_plot.set_ylabel('Proportion of Assembly')
	cdf_plot.set_xlabel('Contig Length')
	plt.show()

if __name__ == '__main__':
	result = remove_n(sys.argv[1])
	plot(result)
