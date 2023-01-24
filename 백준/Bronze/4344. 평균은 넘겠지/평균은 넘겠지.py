C = int(input())
for k in range(C):
    mylist = list(map(int,input().split()))
    N = mylist[0] # list의 첫 번째가 학생수 N임.
    sum = 0
    
    for i in range(1,N+1): # N 제외하고 다 더하기
        sum += mylist[i]
    avg = sum / N 
    ace = 0
    for i in range(1,N+1):
        if (mylist[i] > avg): # 평균을 넘으면 에이스 1개씩 올림
            ace = ace+1 
    print('%0.3f%%' %(ace/N*100)) # 평균 넘는 비율을 소수 3번째 자리 까지 표시