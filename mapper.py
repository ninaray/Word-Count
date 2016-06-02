# Python Exercise 1 - mapper
# June 1, 2016


"""PROGRAM 1: THIS READS AN INPUT FILE, AND PRINTS EACH WORD ON A NEW
LINE, FOLLOWED BY THE NUMBER '1'."""

import sys

def mapper():
    """Prints each word in words on a new line, followed
    by the number '1'."""
        
    for line in sys.stdin:
        line.strip()
        wordarray = line.split(" ")
        
    for word in range(len(wordarray)):
        print(wordarray[word] + ', ' + '1')
        

# Running code
if __name__ == '__main__':
    mapper()