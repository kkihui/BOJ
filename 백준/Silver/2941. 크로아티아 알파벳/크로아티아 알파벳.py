s = input()
slist = list(s)
# print(slist) # slist 확인 용
length = len(s)
# print(length) # length 확인 용
for _ in range(len(s)-1):
    if (slist[_] == 'c' and slist[_+1] == '='):
        #print('c= : -1개')
        length -=1
    
    if (slist[_] == 'c' and slist[_+1] == '-'):
        #print(' c- : -1개')
        length -= 1
            
    if (slist[_] == 'd' and slist[_+1] == '-'):
        #print('d- : -1개')
        length -= 1
            
    if (slist[_] == 'l' and slist[_+1] == 'j'):
        #print('lj : -1개')
        length -= 1
        
    if (slist[_] == 'n' and slist[_+1] == 'j'):
        #print('nj : -1개')
        length -= 1
        
    if (slist[_] == 's' and slist[_+1] == '='):
        #print('s= : -1개')
        length -= 1
        
    if (slist[_] == 'z' and slist[_+1] == '='): #z=이 나온 경우
        if (_ != 0 and slist[_-1] == 'd'): # dz=일 떄
            #print('dz= : -2개')
            length -= 2
        else:
            #print('z= : -1개')
            length -=1 #dz=이 아닌 z=일 떄

print(length)