#!/usr/bin/env python3

import sys

def avg_prob (file_path: str) -> int:
	my_file = None
	line_count = 0
	myquallist = []
	intlist = []
	try:
		my_file = open(file_path, 'r')
		for line in my_file:
			line_count += 1
			if line_count == 4:
				for char in line.strip():
					myquallist.append(ord(char)-33)
		for qual in myquallist:
			intlist.append(1-(10**(-qual)/10))
	finally:
		if my_file != None:
			my_file.close()
	print(sum(intlist)/len(intlist))


if __name__ == '__main__':
	avg_prob(sys.argv[1])
