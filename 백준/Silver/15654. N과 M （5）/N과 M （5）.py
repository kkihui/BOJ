import sys
import itertools
    
def main():
    n,m = map(int,sys.stdin.readline().split())
    numli = list(map(int,sys.stdin.readline().split()))
    numli.sort()
    permutation = itertools.permutations(numli,m)
    for tup in permutation:
        for num in tup:
            print(num,end=' ')
        print('')

if __name__ == '__main__':
    main()