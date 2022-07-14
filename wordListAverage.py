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

