"""Python program to remove all characters except letters and numbers.
keep only a-z, A-Z and 0-9

Everything else (spaces, punctuation, symbols) will be removed.
Without using regular expression 
"""

text = input("Enter a string: ")

result = ""

for char in text:
    if char.isalnum():     # keeps only letters and numbers
        result += char

print(result)

#using regular expression 
import re

text = input("Enter a string: ")

# Replace all NON-alphanumeric characters with empty string
cleantext = re.sub(r'[^A-Za-z0-9]', '', text)

print("Cleaned string:", cleantext)
