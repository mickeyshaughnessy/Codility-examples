# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    lefts = 0
    rights = 0
    if not S:
        return 1
    for char in S:
        if char == '(': #left
            if  rights > 0:
                rights -= 1
            else:
                lefts += 1
        elif char == ')': #right
            if lefts > 0:
                lefts -= 1
            else:
                return 0

    if lefts == 0 and rights == 0:
        return 1
    else:
        return 0
