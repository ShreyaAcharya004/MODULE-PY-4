def count_strings(strings):

    ctr = 0

    
    for word in strings:
        if len(word) >1 and word[0] == word[-1]:
            ctr += 1

    return ctr

print(count_strings(['abc', 'xyz', 'aba', '2221']))countnumberofstrings.py
