# 1. Round a float number to 2 decimal places
Enter_number=float(input("Enter a float number: "))
rounded_number=round(Enter_number, 2)
print("The rounded number is:", rounded_number) 
# 2. Ask for three numbers and output the largest and smallest
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))
largest=max(a, b, c)
smallest=min(a, b, c)
print("The largest number is:", largest)
print("The smallest number is:", smallest)
# 3. Convert kilometers to meters and centimeters
km=float(input("Enter distance in kilometers: "))
m=km*1000
cm=km*100000
print(f"{km} kilometers is equal to {m} meters and {cm} centimeters.")
# Result of integer division and remainder for two numbers
a=int(input("Enter first integer: "))
b=int(input('Enter second integer: '))
c=a//b
d=a%b
print(f'result of integer division: {c}')
print(f'result of remainder: {d}')

# Convert Celsius to Fahrenheit
a=float(input("Enter temperature in Celsius: "))
F=(a*9/5)+32
print(f'{a} Celsius is {F} Fahrenheit.')

# Return the last digit of a number
a=int(input())
n=abs(a)%10
print(f'Last digit of {a} is equal to {n}.')

# 7. Check if a number is even or not
a= int(input('Enter a number: '))
if a%2==0:
    print(f'{a} is an even number.')
else:
    print(f'{a} is not an even number.')    









# STRING QUESTIONS
# 1. Ask name and year of birth, then tell age (current year: 2026)
name=input('write your name, please ^-^: ')
birth_year=int(input('Now enter your year of birth bro) : '))
age=2026-birth_year
print(f'{name} broooo, I know your age. You are {age} years old >-<.')

# 2. Extract car name from txt = 'LMasleitbtui'
txt = 'LMasleitbtui'
car1 = txt[::2] # Every 2nd letter, starting from 0-L
car2=txt[1::2] # Every 2nd letter, starting from 1-M
print(f'The car names are: {car1} and {car2}')

# 3. Length, uppercase, and lowercase of a string
a=input('Enter a string: ')
print(f'Length of the string: {len(a)}')
print(f'Uppercase: {a.upper()}')
print(f'Lowercase: {a.lower()}')

# 4. Check if a string is a palindrome
a=input('Enter a string: ')
b=a.lower()
print(f'{a} is a palindrome: {b==b[::-1]}')

# 5. Count vowels and consonants in a string
a=input('Enter a string: ')
vowels=set('aeiouAEIOU')
vowel_count=sum(1 for char in a if char in vowels)
consonant_count=sum(1 for char in a if char.isalpha() and char not in vowels)
print(f'Number of vowels: {vowel_count}')
print(f'Number of consonants: {consonant_count}')

# 6. Check if one string contains another
main_str= input('Enter the main string: ')
sub_str= input('Enter substring to search for: ')
print('contains substring:', sub_str in main_str)

# 8. Print first and last characters of a string
a = input("Enter a string: ")
if a:
    print("First character:", a[0])
    print("Last character:", a[-1])
else:
    print("String is empty.")

# print reversed version of a string
a = input("Enter a string: ")
print("Reversed string:", a[::-1])

# 10. Count number of words in a sentence
a= input("Enter a sentence: ")
Words= a.split()
print(f"Number of words in the sentence: {len(Words)}")

# 11. Check if a string contains any digits
a = input("Enter a string: ")
contains_digit = any(char.isdigit() for char in a)
print(f"String contains digits: {contains_digit}")


# 12. Join a list of words into a single string separated by a character
words_list = ["Python", "SQL", "Data", "Analytics"]
separator = input("Enter separator (e.g., - or ,): ")
print("Joined:", separator.join(words_list))

# 13. Remove all spaces from a string
s13 = input("Enter a string: ")
print("Without spaces:", s13.replace(" ", ""))

# 14. Check if two strings are equal
str_a = input("Enter first string: ")
str_b = input("Enter second string: ")
print("Are equal:", str_a == str_b)

# 15. Create an acronym from the first letters of each word
sentence = input("Enter a sentence: ")
acronym = ''.join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)

# 16. Remove all occurrences of a specific character from a string
a = input("Enter a string: ")
b = input("Enter a character to remove: ")
print("Result:", a.replace(b, ""))

# 17. Replace all vowels with a symbol (e.g., *)
a = input("Enter a string: ")
b= input("Enter a symbol to replace vowels: ")
vowels = "aeiouAEIOU"
result = ''.join(b if char in vowels else char for char in a)
print("Result:", result)

# 18. Check if a string starts with one word and ends with another
a = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")
if a.startswith(start_word) and a.endswith(end_word):
    print(f"The string starts with '{start_word}' and ends with '{end_word}'.") 
else:
    print(f"The string does not start with '{start_word}' and end with '{end_word}'.")







# Boolean Data Type Questions:

# 1. Check if both username and password are not empty
username = input("Enter username: ")
password = input("Enter password: ")
print("Both non-empty:", bool(username.strip()) and bool(password.strip()))

# 2. Check if two numbers are equal and output a message if they are
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# 3. Check if a number is positive and even
b = int(input("Enter an integer: "))
print("Positive and even:", (b > 0) and (b % 2 == 0))

# 4. Check if three numbers are all different
x1 = float(input("Enter first number: "))
x2 = float(input("Enter second number: "))
x3 = float(input("Enter third number: "))
print("All three are different:", (x1 != x2) and (x2 != x3) and (x1 != x3))

# 5. Check if two strings have the same length
t1 = input("Enter first string: ")
t2 = input("Enter second string: ")
print("Same length:", len(t1) == len(t2))

# 6. Check if a number is divisible by both 3 and 5
a = int(input("Enter an integer: "))
print("Divisible by both 3 and 5:", (a % 3 == 0) and (a % 5 == 0))

# 7. Check if the sum of two numbers is greater than 50
m1 = float(input("Enter first number: "))
m2 = float(input("Enter second number: "))
print("Sum is greater than 50:", (m1 + m2) > 50)

# 8. Check if a given number is between 10 and 20 (inclusive)
kerakmi_shu = float(input("Enter a number: "))
print("Between 10 and 20 (inclusive):", 10 <= kerakmi_shu <= 20)
