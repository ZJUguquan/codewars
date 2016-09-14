'''
Best practice:

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
'''

import math

def isSquare(n):
    sqrt = math.sqrt(n) 
    return (sqrt == int(sqrt))

def find_next_square(sq):
    if( isSquare(sq) ):
        sq += 1
        while( not isSquare(sq) ):
            sq += 1
        return sq
    else:
        return -1