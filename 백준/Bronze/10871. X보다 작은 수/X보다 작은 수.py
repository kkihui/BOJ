N,X = map(int,input().split())
mylist = list(map(int,input().split()))
numlist = list()
# print(mylist) #mylist 잘 들어오나 확인용
for i in range(N):
    if (mylist[i] < X):
        numlist.append(mylist[i]) #integer이므로 extend 말고 append로 추가해ㅑ함.
print(*numlist) # list 앞에 *을 붙히면 괄호 떼고 한 줄로 출력 가능