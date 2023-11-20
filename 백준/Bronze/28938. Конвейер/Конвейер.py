n=input()
a=sum(list(map(int,input().split())))
if a>0:
    b='Right'
elif a<0:
    b='Left'
else:
    b='Stay'
print(b)