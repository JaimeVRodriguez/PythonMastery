sentence = 'This is a common interview question'

letter_dict = {}

for letter in sentence:
    if letter not in letter_dict:
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1


sorted_dict = sorted(letter_dict.items(), key=lambda kv: kv[1], reverse=True)

print(sorted_dict[0])
