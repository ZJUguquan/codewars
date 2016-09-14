'''
Best practice:

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
'''


def valid_parentheses(string):
    balance = 0
    for char in string:
        if(char == "("):
            balance += 1
        if(char == ")"):
            if(balance < 1):
                return False
            balance -= 1
    return True if balance == 0 else False