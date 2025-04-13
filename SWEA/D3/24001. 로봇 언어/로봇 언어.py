# R로 몰거나 L로 몰아서 해보면 됨.
T = int(input())

for t in range(T):
    string = input()
    case = [[],[]]
    dist_max = 0   
    
    for i in range(len(string)):
        if string[i] == '?':
            case[0].append('R')
            case[1].append('L')
        else:
            case[0].append(string[i])
            case[1].append(string[i])
    
    
    for _ in range(2):
    	pos = 0
    	for i in range(len(string)):
            if case[_][i] == 'R':
                pos += 1
            else:
                pos -= 1
            
            dist_max = max(dist_max,abs(pos))
    
    print(dist_max)