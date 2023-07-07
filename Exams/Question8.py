# Ask user for sentence and initializes it to sentence
sentence = input("Input sentence: ")

# counters to count number of letters / numbers
num_letters = 0
num_numbers = 0

# iterates through sentence and counts how many letters
for char in sentence:
    if char.isalpha():
        num_letters += 1

# iterates through sentence and counts how many numbers
for char in sentence:
    if char.isdigit():
        num_numbers += 1

# prints the output
print("LETTERS " + str(num_letters))
print("DIGITS " + str(num_numbers))