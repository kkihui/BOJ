def solution(spell, dic):
    sset = set(spell)
    for d in dic:
        dset = set(d)
        if dset == sset:
            answer = 1
            return answer
    answer = 2
    return answer