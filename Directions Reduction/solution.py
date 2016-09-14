'''
Best practice:

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
'''

def isOpposite(dir1, dir2):
    oppositeMatrix = {
        "EAST": "WEST", 
        "WEST": "EAST",
        "SOUTH": "NORTH",
        "NORTH": "SOUTH"
    }
    if(dir1 == oppositeMatrix[dir2]):
        return True
    else:
        return False

def dirReduc(map):
    for idx, dir in enumerate(map[:-1]):
        if isOpposite(map[idx], map[idx+1]):
            newMap = [val for id, val in enumerate(map) if id not in [idx, idx+1]]
            return dirReduc(newMap)
    return map