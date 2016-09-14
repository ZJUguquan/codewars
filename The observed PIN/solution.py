'''
Best practice:

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
'''


import itertools

def get_adjacent(num):
    matrix = {
        "1": "24",
        "2": "135",
        "3": "26",
        "4": "157",
        "5": "2468",
        "6": "359",
        "7": "48",
        "8": "0579",
        "9": "68",
        "0": "8"
    }
    return matrix[num]

def get_substitutions(pin, position):
    result = list()
    pinList = list(pin)
    for val in get_adjacent(pinList[position]):
        pinList[position] = val
        result.append("".join(pinList))
    return result + [pin]

def get_pins(observed, curpos = 0, acc = None):
    if(acc is None):
        acc = []
    if(curpos > len(observed)-1):
        return []
    comboes = get_substitutions(observed, curpos)
    acc += comboes
    for combo in comboes:
        get_pins(combo, curpos+1, acc)
    res = acc[:]
    return list(set(res))