N = int(input())
mylist = list(map(int,input().split()))
mylist.sort() # 오름차순으로 정리하기
print(str(mylist[0])+' '+str(mylist[N-1]))