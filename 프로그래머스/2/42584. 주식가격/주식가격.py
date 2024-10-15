# N = 100,000 이므로 O(NlogN) 이하의 코드를 짜야함.
def solution(prices):
    stack = []
    answer = list(range(len(prices)-1,-1,-1))
    reprices = []
    
    # idx값과 price를 지닌 reprice 생성
    for i in range(len(prices)):
        reprices.append((i,prices[i]))
    
    # Stack 활용해서 감소하는 애들 반영
    for i in range(len(prices)):
        if len(stack) >= 1:
            while stack[-1][1] > reprices[i][1]:
                idx = stack.pop()[0]
                answer[idx] = i-idx
                if len(stack) == 0:
                    break
        stack.append(reprices[i])
    
    return answer