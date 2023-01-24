N = int(input())
com = 0 # 합성수
num_list = list(map(int,input().split()))
num_list.sort()
my_list = list(range(2,1001)) # 2~1000까지의 list
# print(num_list) # 처음에 받은 수 목록 확인용
for i in range(N): # num_list[0]~num_list[N-1] 까지 반복함.
    # print(num_list[i]) # 순서 확인용
    if num_list[i] != 1 : #숫자가 1이 아니라면
        my_list.remove(num_list[i]) # 자기 자신 지워줌
    else: #숫자가 1이면 합성수 하나 올려줘야 함
        com += 1
    # print(my_list) #잘 나오나 확인용
    for k in my_list: # 2~1000으로 나눠봄
        if num_list[i] % k == 0: #나눠 떨어지면 합성수 하나 올리고 정렬 후에 탈출
            com += 1
            my_list.append(num_list[i]) # 다시 지워줬던 수 넣어주고 정렬하기
            my_list.sort()
            break
        
    if num_list[i] != 1: #탈출 못한 경우, 숫자가 1이 아니라면
        my_list.append(num_list[i]) # 다시 지워줬던 수 넣어주고 정렬하기
        my_list.sort()            
dec = N - com # 소수 개수 = 받은 개수-합성수 개수 
print (dec)