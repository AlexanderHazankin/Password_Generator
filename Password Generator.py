import random
import string

letters = string.ascii_letters
numbers = list(map(str, range(0, 10)))
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

random_list = []

random_letter = random.choice(letters)
random_number = random.choice(numbers)
random_symbol = random.choice(symbols)

for letter in range(nr_letters):
    random_letter = random.choice(letters)
    random_list.append(random_letter)
for number in range(nr_numbers):
    random_number = random.choice(numbers)
    random_list.append(random_number)
for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    random_list.append(random_symbol)

random.shuffle(random_list)
print(''.join(random_list))
