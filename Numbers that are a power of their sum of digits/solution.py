'''
Best practice:

series = [0]
for a in range(2, 99):
    for b in range(2, 42):
        c = a**b
        if a == sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__
'''

def DigitSum(n):
    nString = str(n)
    result = 0
    for digit in nString:
        result += int(digit)
    return result

def DigitSum1(x):#can be faster
    s=0
    x1=x
    while(x1>0):
        s+=x1%10
        x1=x1/10
    return s

def power_sumDigTerm(n):
    resultTable = list()
    for i in range(2, 100):
        value = i
        for j in range(2, 20):
            value *= i
            if(DigitSum(value) == i):
            #if(DigitSum1(value) == i):
                resultTable.append(value)
    resultTable.sort()
    return resultTable[n-1] # n-th term of the sequence, each term is a power of the sum of its digits
