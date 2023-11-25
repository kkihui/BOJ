# 전화번호부 최대 크기는 100만 이하 (각각을 20번 이하로 연산해야 함)
# O(n^2) 이상은 안 됨. O(nlogn) 이하의 알고리즘 필요
# 각각의 길이만큼 앞에서 잘라주는 dictionary 만들어서 같은거 있으면 False 뽑게 하기.

def solution(phone_book):
    min_len = 21
    max_len = 0
    
    for i in range(len(phone_book)):
        length = len(phone_book[i])
        if length > max_len:
            max_len = length
        if length < min_len:
            min_len = length
    
    for i in range(min_len,max_len+1):
        ndict = dict()
        for j in range(len(phone_book)):
            if len(phone_book[j]) >= i: # 지금 판단하고자 하는 길이이상을 가진 단어만 체크
                s = phone_book[j][:i]
                if s in ndict:
                    if ndict[s] == i or len(phone_book[j]) == i: # 앞에만 같은거 방지
                        answer = False
                        return answer
                else:
                    ndict[s] = len(phone_book[j])    
    answer = True
    return answer