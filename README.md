# PyPassword Generator
Welcome to the PyPassword Generator!
This script allows you to generate a random password with a desired number of letters, numbers, and symbols.

This is a Python script that generates a random password by asking the user for the number of letters, numbers, and symbols they want in their password.
The script uses the string module to get a string of all the ASCII letters (upper-case and lower-case), the range() function to create a list of numbers from 1 to 9, and a list of symbols.
It then uses the random.choice() function to randomly select a letter, number, and symbol from these lists and adds them to a random_list list.
The script then shuffles the elements in the list using the random.shuffle() function and finally prints the password by joining the elements in the list.

## Getting Started
To use the PyPassword Generator, simply run the script in your Python environment and follow the prompts.
You will be asked to enter the number of letters, numbers, and symbols you want in your password.
The script will then generate a random password and print it to the console.

## Requirements
Requires Python 3.x to run.

## Credits
Created by Alexander Hazankin.

## Contact
For any questions or comments, you can reach me at:

https://www.linkedin.com/in/hazankin

https://github.com/AlexanderHazankin

https://replit.com/@Hazankin

## License
This project is licensed under the MIT License.

Copyright (c) 2022 Alexander Hazankin.

Permission is hereby granted, free of charge.

## NOTE:
This is one of my exercises from Udemy online Course: "100 Days of Code: The Complete Python Pro Bootcamp for 2022" by Dr. Angela Yu

## Acknowledgments
The 'random' and 'string' modules were used to generate the random password.
The 'map()' and 'join()' functions were used to convert lists to strings and combine the password elements.

## Example
Welcome to the PyPassword Generator!
How many letters would you like in your password?
3
How many numbers would you like?
2
How many symbols would you like?
1
K5#T8a
