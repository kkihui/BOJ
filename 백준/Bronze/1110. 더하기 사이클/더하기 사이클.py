import copy
n=int(input())
c=copy.deepcopy(n)
b=0
while True:
    if n<10:
        n = n*11
        b += 1
        if n==c:
            break
    
    else:
        a=n//10+n%10
        n=10*(n%10)+a%10
        b += 1
        if n==c:
            break
print(b)