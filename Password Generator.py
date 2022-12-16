import random
import string

# import the ascii letters and numbers, as well as a list of symbols
letters = string.ascii_letters
numbers = list(map(str, range(0, 10)))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print a welcome message
print("Welcome to the PyPassword Generator!")

# ask the user how many letters, numbers, and symbols they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# create an empty list to store the randomly selected characters
letter_list = []

# select a random letter, number, and symbol to start
random_letter = nr_letters
random_number = nr_numbers
random_symbol = nr_symbols

# add the desired number of random letters to the list
for letter in range(nr_letters):
    letter_list += random.choice(letters)

# add the desired number of random numbers to the list
for number in range(nr_numbers):
    letter_list += random.choice(numbers)

# add the desired number of random symbols to the list
for symbol in range(nr_symbols):
    letter_list += random.choice(symbols)

# shuffle the list of characters
random.shuffle(letter_list)

# convert the letter_list to a string and assign it to the password variable
password = "".join(letter_list)
print(password)
