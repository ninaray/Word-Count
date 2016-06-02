# Python Exercise 1 - reducer
# June 1, 2016


"""PROGRAM 2: THIS READS PROGRAM 1'S OUTPUT FILE, AND PRINTS EACH WORD
(WITHOUT REPEATS), FOLLOWED BY THE NUMBER OF TIMES IT OCCURS. """

import sys

def reducer():
    """Prints each word in words on a new line, followed
    by the number of times it occurs."""
    
    newarray = []
    
    for line in sys.stdin:
        line.strip() #Clean each line, EX: 'A, 1' 'a, 1' 'ago, 1'
        linearray = line.split(", ") #Add word + count to array each time, EX: ['A', '1', 'a', '1', 'ago', '1']
        number = linearray[1]
        linearray[1] = number[:len(number) - 1]
        for l in linearray:
            newarray.append(l)
        
    #Numbers will always be in odd indices
        
    #EX: ['Episode', '1', 'far', '1', 'far', '1in', '1']
    i = 0
    while i < len(newarray) - 1:
        compare = newarray[i]
        for k in range(i+2, len(newarray)):
            if compare == newarray[k]:
                newarray[i+1] = str(int(newarray[i+1]) + 1)
            
        i = i + 2
            
        #['Episode', '1', 'far', '1', 'far', '1', 'in', '1']
        #['Episode', '1', 'far', '2', 'far', '1', 'in', '1']
        #['Episode', '1', 'far', '2', 'far', '1', 'in', '1']        
    
    updatedarray = []
    n = 0
    while n < len(newarray) - 1:
        if newarray[n] not in updatedarray:
            updatedarray.append(newarray[n])
            updatedarray.append(newarray[n+1])
        n = n + 2
        
        #[]
        #['Episode', '1']
        #['Episode', '1', 'far', '2']
        #['Episode', '1', 'far', '2']
        #['Episode', '1', 'far', '2', 'in', '1']
        
    element = 0
    while element < len(updatedarray) - 1:
        print(updatedarray[element] + ', ' + updatedarray[element + 1])
        element = element + 2
        
# Running code
if __name__ == '__main__':
    reducer()
