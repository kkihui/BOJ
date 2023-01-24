import sys

def check(s): #그룹 단어 인지 확인하는 함수
    sli = list(s)
    for i in range(26): #a~z까지 해봄
        a = sli.count(chr(i+97))
        ali= []
        
        if sli.count(chr(i+97)) > 1: # 글자가 2번 이상 나오면
            for k in range(a): # 몇 번 째로 나왔는지 리스트 만듦
                ali.append(sli.index(chr(i+97)))
                sli[sli.index(chr(i+97))] = 0
                
            for k in range(a-1): # 그 리스트가 1씩 차이 안 나면 그룹 단어 아님
                b = ali[k+1]-ali[k]
                if b != 1:
                    return 0
    return 1 # 그 외의 경우는 그룹 단어 맞음
    
result = 0
N=int(sys.stdin.readline().rstrip())
for _ in range(N):
    result += check(sys.stdin.readline().rstrip())
print(result)    