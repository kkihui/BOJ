mylist = list(input())
for i in range(len(mylist)):
    if mylist[i] != mylist[len(mylist)-1-i]: #앞의 글자와 반대편의 글자가 다르다면 palindrome 아님
        palind = False
        break
    else: # 앞의 글자와 반대편의 글자가 다 같으면 palindrome임
        palind = True 
print(int(palind))