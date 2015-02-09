# you can use print for debugging purposes, e.g.
# print "this is a debug message"

# The strategy is to iterate through the string, putting each character onto 
# a specific stack, depending on its type.
# A, When we put the character onto the stack, we check to see if the one before it
# is an opposite - eg. { then } are opposites. If we find an opposite pair, we annihilate them. 
# When a pair is annihilated, we check to see if any other types have priority

# The strategy is to iterate through the array, putting each character onto the stack. If the opposite character is present on the stack, immediately annihilate both. At the end if the size of the stack is zero, the string is properly formatted. 

def solution(S):
    annihilate = {
        ')': '(',
        ']': '[',
        '}': '{',
        }
        
    stack = []
    if not S:
        return 1
    for char in S:
        #print char
        if char in annihilate.keys() and len(stack) > 0:
            if stack[-1] == annihilate[char]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
        #print stack
    if len(stack) == 0:
        return 1
    else:
        return 0
