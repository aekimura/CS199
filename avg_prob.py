#!/usr/bin/env python3

import sys

def avg_prob (file_path: str) -> int:
	my_file = None
	line_count = 0
	myquallist = []
	try:
		my_file = open(file_path, 'r')
		for line in my_file:
			line_count += 1
			if line_count == 4:
				for char in line.strip():
					myquallist.append(1-(10.0**(-(ord(char)-33)/10.0)))
	finally:
		if my_file != None:
			my_file.close()
	print(sum(myquallist)/len(myquallist))


if __name__ == '__main__':
	avg_prob(sys.argv[1])
