#!/bin/python3

import sys

def main():

    curPage = None
    pageCount = 0
    pageSize = 0

    for line in sys.stdin:

        line = line.strip().split() # remove newlines and split the line
        page = line[0] # grab the page name
        count = int(line[1]) # grab the count
        size = int(line[2]) # grab the size

        # add to count and size if we get a same page
        if page == curPage:
            pageCount += count
            pageSize += size
        else:
            # otherwise, print out the count of the current page
            if curPage:
                print(f'{curPage}' + '{visits} ' + str(pageCount))
                print(f'{curPage}' + '{size} ' + str(pageSize))

            # update the page, count, and size
            pageCount = count
            pageSize = size
            curPage = page

    # print out the final page seen
    if curPage == page:
        print(f'{curPage}' + '{visits} ' + str(pageCount))
        print(f'{curPage}' + '{size} ' + str(pageSize))

if __name__ == '__main__':
    main()
