def solution(arr):
    stack = []
    for n in arr:
        if len(stack) != 0:
            if stack[-1] != n:
                stack.append(n)
        else:
            stack.append(n)
    answer = stack
    
    return answer