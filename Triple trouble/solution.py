'''
Best practice:

def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])
'''


from itertools import groupby

def get_groups(n, size):
    return [g for g,l in groupby(n) if len(list(l)) >= size and g != 0]

def triple_double(num1, num2):
    groups1 = get_groups(str(num1), 3)
    groups2 = get_groups(str(num2), 2)
    resultList = [value for value in groups1 if value in groups2]
    return 1 if resultList else 0