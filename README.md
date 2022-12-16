# Password_Generator
 A password generator is a tool that automatically creates a strong and unique password. 

This can be useful for creating secure passwords that are difficult for others to guess.
To use a password generator, you simply need to specify the length and type of characters you want the password to contain,
and the generator will create a password for you. Some password generators may also have additional options,
such as the ability to exclude certain characters or to generate passwords that are easy for humans to remember.

This is one of my exercises from Udemy online Course: "100 Days of Code: The Complete Python Pro Bootcamp for 2022" by Dr. Angela Yu

# for developers:
This is a Python script that generates a random password by asking the user for the number of letters, numbers, and symbols they want in their password.
The script uses the string module to get a string of all the ASCII letters (upper-case and lower-case), the range() function to create a list of numbers from 1 to 8, and a list of symbols.
It then uses the random.choice() function to randomly select a letter, number, and symbol from these lists and adds them to a random_list list.
The script then shuffles the elements in the list using the random.shuffle() function and finally prints the password by joining the elements in the list.