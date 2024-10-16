# N,M은 8이하이므로 최대 1640개 (8P4)

import sys
import itertools
    
def main():
    n,m = map(int,sys.stdin.readline().split())
    num_list = list(map(int,sys.stdin.readline().split()))
    
    permutation = itertools.permutations(num_list,m)
    per_set = set(permutation)
    perli = sorted(list(per_set))
    
    for tup in perli:
        for num in tup:
            print(num,end=' ')
        print('')

if __name__ == '__main__':
    main()