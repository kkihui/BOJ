def jong(a):
    end = False
    i = 0
    count = 0
    while end == False:
        if count == a:
            end == True
            break
        else:
            if i%1000==666:
                count += 1
                number = i
            elif (i//10)%1000==666:
                count += 1
                number = i
            elif (i//100)%1000==666:
                count += 1
                number = i
            elif (i//1000)%1000==666:
                count += 1
                number = i
            elif (i//10000)%1000==666:
                count += 1
                number = i
            elif (i//100000)%1000==666:
                count += 1
                number = i
            elif (i//100000)%1000==666:
                count += 1
                number = i
        i = i+1
    return(number)

N = int(input())
print(jong(N))
