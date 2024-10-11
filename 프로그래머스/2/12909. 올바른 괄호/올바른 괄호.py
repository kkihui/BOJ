def solution(s):
    stack = []
    
    for character in s:
        if character == "(":
            stack.append(character)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
            
    if len(stack) == 0:
        return True
    else:
        return False