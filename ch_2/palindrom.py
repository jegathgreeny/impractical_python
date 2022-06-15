"""Find palindromes (letter palingrams) in a dictionary file."""

import dictionary

# The dictionary library returns a list of words.
word_list = dictionary.load('dictionary/dictionary.txt')
palindrome_list = []

for word in word_list:
    # In [1:1:1] the first '1' states the starting position.
    # Then the second '1' states the ending position.
    # Then the third '1' is the stepting element.
    # In this case the stepping element is '-1' which means to slice the word in reverse.
    if len(word) > 1 and word == word[::-1]:
        palindrome_list.append(word)


print(f"Number of palindromes found = {len(palindrome_list)}.")
# The '*' gives a nice readable output.
print(*palindrome_list, sep='\n')
