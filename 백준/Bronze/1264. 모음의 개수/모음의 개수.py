while True:
    s = input()
    if s == '#':
        break
    else:
        s = s.lower()
        count = 0
        for _ in range(len(s)):
            if s[_] in 'aeiou':
                count += 1
        print(count)