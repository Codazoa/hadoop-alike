#!/bin/python3

import sys

def main():
    # get each line
    for line in sys.stdin:
        # get rid of \n and split the words
        line = line.strip().split()

        # if the line is valid
        if line[3] == 'T':
            # print first 3 terms to stdout
            print(" ".join(line[:3]))

if __name__ == '__main__':
    main()
