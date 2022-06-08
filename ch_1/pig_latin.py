"""Turn a word into its pig latin equivalent."""

VOWELS = "aeiouy"

# the word from the user
word = input("Type a word and get its pig latin equivalent: ")

if word[0] in VOWELS:
    pig_latin = word + "way"

else:
    pig_latin = word[1:] + word[0] + "ay"

print(pig_latin)
