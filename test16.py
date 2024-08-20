def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i in other_words or other_words in i:
            same_words.append(i)
    return same_words


result1 = single_root_words('boobs', 'blue', 'orangered', 'pink')
result2 = single_root_words('Toruviel', 'Dhoine', 'Dwarf', 'Luned')

print(result1)
print(result2)
