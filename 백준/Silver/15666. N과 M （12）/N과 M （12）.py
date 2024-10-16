import sys
import itertools
    
def main():
    n,m = map(int,sys.stdin.readline().split()) 
    num_set = set(map(int,sys.stdin.readline().split()))
    combination_replace = itertools.combinations_with_replacement(num_set,m)
    answer = []
    for combi in combination_replace:
        answer.append(sorted(list(combi)))
    answer.sort()
    
    for tup in answer:
        for num in tup:
            print(num,end=' ')
        print('')

if __name__ == '__main__':
    main()