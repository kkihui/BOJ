import itertools
import math

def solution(clothes):
    cloth_dic = {}
    
    # 종류 별로 몇 개 있는 지 파악
    for _ in range(len(clothes)):
        if clothes[_][1] in cloth_dic:
            cloth_dic[clothes[_][1]] += 1
        else:
            cloth_dic[clothes[_][1]] = 1
    
    # 옷의 종류, 각 종류 별 몇개 있는지 저장
    cloth_kind = len(cloth_dic)
    cloth_li = list(cloth_dic.values())
    cloth_sum = sum(cloth_li)
    
    # 옷 종류의 조합 찾고 거기서 옷의 조합 계산 (ex. 3C3 -> 3C2 -> 3C1)
    combi_num = cloth_kind
    answer = 0
    
    # 다 1개 씩 있으면 조합의 수만 계싼
    if cloth_kind == cloth_sum:
        while combi_num > 0:
            answer += math.comb(cloth_kind,combi_num)
            combi_num -= 1
    
    else:
        while combi_num > 0:
            # 옷 종류의 조합
            # kind_li = list(itertools.combinations(range(cloth_kind), combi_num))
            kind_li = list(itertools.combinations(cloth_li, combi_num))

            # 종류의 조합에 따른 옷의 조합
            for kind in kind_li:
                if kind == [1]*len(kind):
                    answer += 1
                else:
                    num = 1
                    for cloth_num in kind:
                        num *= cloth_num
                    answer += num
            combi_num -= 1

    return answer