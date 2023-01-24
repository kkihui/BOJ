def evenpalindrome(a):
    l = len(a)
    for _ in range(l):# 앞의 글자와 반대편의 글자가 다르면 palindrome 아님
        if a[_] != a[l-1-_]:
            return False 
    if l%2 == 1: # palindrome이 odd면 oddpalindrome
        return False
    else: # even이 있으면 even palindrome
        return True
s = input()
r = len(s)
slist = []
for _ in range(r):#처음과 끝이 같은 substring다 찾음
    for i in range(_+1,r):
        if s[_] == s[i]:
            slist.append(s[_:i+1])
odd = True
for _ in slist:
    if evenpalindrome(_) == True:
        odd = False
        print('Or not.')
        break
if odd == True:
    print('Odd.')