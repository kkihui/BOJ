import sys

def arimean(li):
    res = sum(li)/len(li)
    if (res*10)%10 == 5:
        res = int(res)+1
    else:
        res = int(round(res))
    return res    

def median(li):
    return li[(len(li)-1)//2]

def mode(li):
    countli = [0]*8001

    for _ in li:
        countli[_] += 1
    
    if countli.count(max(countli)) == 1:
        if countli.index(max(countli)) <= 4000:
            res = countli.index(max(countli))
        else:
            res = countli.index(max(countli))-8001
    else:
        modeli=[]
        count = max(countli)
        for _ in range(8001):
            if countli[_] == count:
                if _ <= 4000:
                    modeli.append(_)
                else:
                    modeli.append(_-8001)
        modeli.sort()
        res = modeli[1]
    return res
    
def bounds(li):
    return max(li) - min(li)

n = int(sys.stdin.readline())
numli = [0]*n
for _ in range(n):
    numli[_] = int(sys.stdin.readline())
numli.sort()

print(arimean(numli))
print(median(numli))
print(mode(numli))
print(bounds(numli))