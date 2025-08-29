def length_of_last_word(s):
    words = [' ']
    words.extend(s)
    i = len(words) - 1
    while words[i]==' ':
        i -= 1
    hi = i
    while words[i]!=' ':
        i -= 1
    return hi - i




