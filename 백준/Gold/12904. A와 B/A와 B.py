import sys

def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    word = t
    length = len(t)
    
    while length != len(s):
        if word[length-1] == 'A':
            word = word[:-1]
        else:
            word = ''.join(reversed(word[:-1]))
        length -= 1
        
    if s == word:
        print(1)
    else:
        print(0)
    
        
if __name__ == "__main__":
    main()