T = int(input())
for i in range(T):
    n,s = input().split()
    slist = list(s)
    qlist = []
    # print(slist) # slist 확인용
    for k in range(len(slist)): # slist에 글자들을 n회 반복시켜서 qlist로 만듦
        qlist.extend(slist[k]*int(n)) 
    # print(qlist) # qlist 확인용
    q = ''.join(qlist) #리스트를 다시 문자열로
    print(q)