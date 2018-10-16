#!/usr/bin/env python3

import sys

def count_lines(file_path: str) -> int:
    '''Returns the number of lines in a file'''
    the_file = None
    try:
        the_file = open(file_path, 'r')
        line_count = 0
        for line in the_file:
            line_count += 1
        print(line_count)
    finally:
        if the_file != None:
            the_file.close()

if __name__ == '__main__':
    count_lines(sys.argv[1])

