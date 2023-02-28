sentence = 'This is a common interview questions'

letters = [i for i in sentence if i != ' ']
counts = {}

for letter in letters:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

max_val = None
max_key = None

for key, val in counts.items():
    if max_val is None or val > max_val:
        max_val = val
        max_key = key

print(f'{max_key}: {max_val}')