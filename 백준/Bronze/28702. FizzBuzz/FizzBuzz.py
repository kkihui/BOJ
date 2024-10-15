import sys

fizz = list()
num = 0

for i in range(3):
    fizz.append(sys.stdin.readline().rstrip())
    if fizz[i].isnumeric():
        num = int(fizz[i]) + 3 - i

if num != 0:
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if num % 5 == 0:
            print("Buzz")
        else:
            print(num)
                  