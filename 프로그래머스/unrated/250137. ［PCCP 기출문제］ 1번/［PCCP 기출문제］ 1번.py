def solution(bandage, health, attacks):
    lastt = attacks[-1][0]
    atcnt = 0
    conti = 0
    hp = health
    for t in range(1,lastt+1):
        if t == attacks[atcnt][0]:
            hp -= attacks[atcnt][1]
            atcnt += 1
            conti = 0
            if hp <= 0:
                answer = -1
                return answer
        else:
            conti += 1
            hp += bandage[1]
            if conti == bandage[0]:
                hp += bandage[2]
                conti = 0
            hp = min(hp,health)                
    
    answer = hp
    
    return answer