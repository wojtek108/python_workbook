def wordList(lista):
    total = 0
    short = len(lista[0])
    long = len(lista[0])
    for word in lista:
        if len(word) < short:
            short = len(word)
        if len(word) > long:
            long = len(word)
        total = total + len(word)
        result = total/len(lista)
    return long, short, result

print(wordList(['tomek', 'michal', 'wg', 'michalski']))


# I didn´t know the min() and max() methods which make for a more pythonic solution as demonstrated by Reuven

def summarize(words):
    word_lengths = [len(one_word)
                    for one_word in words]

    return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)


print(summarize(['tomek', 'michal', 'wg', 'michalski']))
