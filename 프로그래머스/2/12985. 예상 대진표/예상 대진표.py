def solution(n,a,b):
    answer = 1
    while True:
        if (b-a == 1 and b%2 == 0) or (b-a == -1 and a%2 == 0):
            return answer
        else:
            if b%2 == 1:
                b = (b+1)//2
            else:
                b //= 2

            if a%2 == 1:
                a = (a+1)//2
            else:
                a //= 2
            answer += 1