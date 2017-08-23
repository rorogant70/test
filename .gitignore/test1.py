def test(word, wordList):
    countries 
    first = 0
    last = len(wordList) - 1
    found = False
    while first <= last and not found:
        middle = (first + last)//2
        if wordList[middle] == word:
            found = True
        else:
            if word < wordList[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found
