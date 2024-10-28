# 글자 받으면 모음인지 자음인지 구분
# 최대 5개의 모음, 10개의 자음으로 7의 길이를 지닌 것 -> 15C7 = 6435

import sys
import itertools

def main():
    l,c = map(int,sys.stdin.readline().split())
    char_list = list(map(str,sys.stdin.readline().split()))
    vowels = set(['a','e','i','o','u'])
    given_vowel = set()
    given_conso = set()
    ans = set()
    
    for c in char_list:
        if c in vowels: given_vowel.add(c)
        else: given_conso.add(c)
    
    # 길이가 l인 조합 싹다 만들기
    for combi in itertools.combinations(char_list,l):
        # 모음 개수, 자음 개수 판단
        vowel_cnt = 0
        conso_cnt = 0
        for char in combi:
            if char in vowels: vowel_cnt += 1
            else: conso_cnt += 1 
        
        if conso_cnt >= 2 and vowel_cnt >= 1:
            ans.add(''.join(sorted(combi)))
        
    for result in sorted(ans):
        print(result)
        
if __name__ == "__main__":
    main()

''' 자음 2개 모음 1개 뽑지 말고 다 하고 나서 모음,자음 카운팅 하는 방식 써보기
# 글자 받으면 모음인지 자음인지 구분
# 최대 5개의 모음, 10개의 자음으로 9의 길이를 지닌 것 -> 5c1 * 10C2 * 13c6 = 5*45*1716 = 최대 386,100

import sys
import itertools

def main():
    l,c = map(int,sys.stdin.readline().split())
    char_list = list(map(str,sys.stdin.readline().split()))
    vowels = set(['a','e','i','o','u'])
    given_vowel = set()
    given_conso = set()
    ans = set()
    
    for c in char_list:
        if c in vowels:
            given_vowel.add(c)
        else:
            given_conso.add(c)
    
    
    consoC2 = itertools.combinations(given_conso,2)
    vowelC1 = itertools.combinations(given_vowel,1)
    
    # 모음 하나 선택
    for vowel in vowelC1:
        # 자음 둘 선택
        for conso1,conso2 in consoC2:
            basis = set((conso1,conso2,vowel[0]))
            # 나머지 선택해서 나머지로 (글자-3)C(길이-3) 해서 더하기
            rest_char = set(char_list) - basis
            rest_combi = itertools.combinations(rest_char,l-3)
            
            for rest in rest_combi:
                result = sorted(basis.union(rest))
                print(result)
                ans.add(''.join(result))
    
    for result in sorted(ans):
        print(result)
        
if __name__ == "__main__":
    main()
'''