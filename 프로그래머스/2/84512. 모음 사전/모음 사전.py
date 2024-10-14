def solution(word):
    word_list = ['A','E','I','O','U']
    word_dict = {}
    
    for i in range(1,5):
        for w in word_list:
            if len(w) == i:
                for j in range(5):
                    word_list.append(w+word_list[j])
    word_list.sort()
    for i in range(len(word_list)):
        word_dict[word_list[i]] = i+1
    
    return word_dict[word]