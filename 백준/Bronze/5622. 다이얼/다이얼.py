s = input()
slist = list(s)
t = 0
for i in range(len(s)):
    a = ord(slist[i])-65 #아스키 코드에서 65 빼서 저장
    if a <= 17 or a==19 or a==20 or a==22 or a==23 : # R 밑의 글자들과 T,U,W,X의 경우
        t += a//3+3 # ABC의 경우는 0,1,2이므로 2초라서 +3   
    elif a == 18 or a == 21 or a==24 or a==25 : # S,V,Y,Z의 경우
        t += a//3+2
print(t)