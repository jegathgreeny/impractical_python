"""Map letters from string into dictionary & print bar chart for frequency."""

import pprint
import sys
from collections import defaultdict

# the sentence from the user
sentence = input("Enter a sentence: ")

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

mapped = defaultdict(list)

for character in sentence:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)

# pprint lets you print stacked output.
print("text = ", end="")
print(f'{sentence}', file=sys.stderr)
pprint.pprint(mapped, width=200)
