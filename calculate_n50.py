#!/usr/bin/env python3

import sys

def get_contigs (file_path) -> list:
	contigs = []
	my_file = None
	n50 = 0
	try:
		my_file = open(file_path, 'r')
		for line in my_file:
			try:
				length = (int(line.split()[1]))
				#print(length)
				contigs.append(length)
			except:
				next
	finally:
                if my_file != None:
                        my_file.close()
	return contigs

def calculate_n50(contigs) -> int:
	contigs.sort()
	halfcontigs = sum(contigs)/2
	print(halfcontigs)
	n50 = 0
	for contig in contigs:
		if n50 < halfcontigs:
			n50 += contig
			if n50 > halfcontigs:
				return contig


if __name__ == '__main__':
        print(calculate_n50(get_contigs(sys.argv[1])))



