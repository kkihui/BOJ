import math

def hansu(a): #한수인지 판단하는 함수 solve() 정의
    if (a//100 == 0): #100이하는 전부 한 수
        ans =1 
    else:
        b = int(math.log10(a)//1)
        mylist = list()
        for i in range(b+1): # a의 자리수 개수 만큼 쪼개기
            mylist.append(a//(10**i)%10)
        # print(mylist) # my list 제대로 나오는지 확인용
        for i in range(b-1):# a의 자리수-2번 만큼 반복
            if (mylist[i+1] - mylist[i] != mylist[i+2] - mylist[i+1]): #공차가 다르다면 한수가 아니니까 탈출
                ans = 0
                break
            else: # 공차가 끝까지 같다면 한수 맞음
                ans = 1
    
    return ans

N = int(input())
sum = 0
for k in range(1,N+1): #전부다 한수인지 판단해서 한수 일 때 마다 sum 올려줌
    sum += hansu(k) 
print(sum)