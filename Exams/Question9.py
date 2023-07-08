# Ask user for sentence and initializes it to sentence
sentence = input("Input sentence: ")

# counters to count number of uppercase / lowercase letters
uppercase_letters = 0
lowercase_letters = 0

# iterates through sentence and counts how many uppercase and lowercase letters
for char in sentence:
    if char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1

# prints the output
print(f"UPPER CASE {uppercase_letters}")
print(f"LOWER CASE {lowercase_letters}")
