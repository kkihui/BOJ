S = int(input())
sum,i = 0,0
while sum <= S: # S가 1~N 까지의 합과 1~N+1까지의 합 사이에 있으면, S는 1~N-1과 N+a를 통해서 N개의 합으로 표현 가능
    i += 1
    sum = i*(i+1)/2 #1~i까지의 합
print(i-1)