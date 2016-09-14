'''
Best practice:

def parse_float(string):
    try:
        return float(string)
    except:
        return None
'''

def parse_float(string):
    try:
        [high, low] = string.split(".")
    except Exception:
        return None
    else:
        highInt = int(high)
        lowInt = int(low)
        return highInt + (lowInt / (10 **len(low)))