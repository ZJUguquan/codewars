'''
Best practice:

def scale_horizontal(strng,k):
    retstrng = strng
    if k > 1:        
        s = [s*k for s in strng]
        retstrng = "".join(s)
    return retstrng


def scale(strng, k, n):
    if strng == "": return ""
    lines = strng.split('\n')    
    lines = [scale_horizontal(line,k) for line in lines]
    retlines = []
    for i in range(len(lines)):
        for j in range(n):
            retlines.append(lines[i])
    return "\n".join(retlines)
'''


def scale(string, k, n):
    if not string:
        return ''
    result = []
    for row in string.split("\n"):
        newRow = []
        for char in row:
            newRow.append( "".join( [char for i in range(k)] ) )
        result.append( "\n".join(["".join(newRow) for j in range(n)]) )
    return "\n".join(result)