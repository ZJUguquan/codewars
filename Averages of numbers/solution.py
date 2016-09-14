'''
Best practice:

def averages(arr):
    return [(arr[x]+arr[x+1])/2 for x in range(len(arr or [])-1)]
'''

def averages(arr):
    try:
        result = []
        for id, element in enumerate(arr[:-1]):
            result.append( (arr[id]+arr[id+1])/2 )
        return result
    except Exception:
        return []