a = True
while a==True:
    s= input()
    if s == '0':
        a = False
        break
    else:
        l = len(s) 
        for i in range(l):
            if s[i] != s[l-1-i]:
                palind = False
                break
            else: 
                palind = True
    if palind == True:
        print('yes')
    else:
        print('no')