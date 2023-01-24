from copy import deepcopy #deepcopy 사용위해 들고옴

mylist = list()
for i in range(9):
    mylist.append(int(input()))
mylist2 = deepcopy(mylist) #정렬하기 전에 원래  list 복사 
mylist.sort() # 오름차순으로 정리하기
# print(mylist) # mylist 확인용
print(mylist[8]) # 제일 큰 수 출력
print(mylist2.index(mylist[8])+1) # 제일 큰 수 있던 위치 출력 (list에서의 위치 니까 +1)