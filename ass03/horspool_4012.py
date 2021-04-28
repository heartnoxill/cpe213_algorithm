# Horspool string matching
# Consist of ShiftTable() and HorspoolMatch()
import sys
__author__ = "Pattarapon Buathong 62070504012"

global size
global cnt
global table
size = 256 # a A

def shiftTable(pattern):
    table = [0]*size
    m = len(pattern)
    for i in range(size-1):
        table[i] = m
    for j in range(m-2):
        table[pattern[j]] = m-1-j
    return table

def horspoolMatch(pattern, text):
    m = len(pattern)
    n = len(text)
    table = shiftTable(pattern)
    cnt = 0
    i = m-1

    while i <= n-1:
        k = 0
        while (k <= m-1) and (pattern[m-1-k] == text[i-k]):
            k += 1
        if k == m:
            cnt += 1
            print("Pattern {} found in position: {}".format(pattern,cnt))
            return i-m+1
        else:
            i += table[ord(text[i])]
            cnt += 1
            print("Number of comparisons made: {}".format(cnt))
    print("Pattern {} not found".format(pattern))
    return -1

if __name__ == '__main__':
    text = input("Enter a text to search (or key'q' to exit): ")
    if text == 'q':
        print("End of Program\n")
        sys.exit()
    pattern = input("Enter a pattern to search: ")
    horspoolMatch(pattern, text)