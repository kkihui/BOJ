import sys
while True:
    customer = list(map(str,sys.stdin.readline().split()))
    if customer[0] == '#':
        break
    else:
        if int(customer[1]) > 17 or int(customer[2]) >= 80:
            a = 'Senior'
        else:
            a = 'Junior'
        print(customer[0],a)