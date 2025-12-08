import re
def stringmatch(str):
        pattern = '^[a-zA-Z0-9_]*$'
        if re.search(pattern,  str):
                return 'Found a match!'
        else:
                return('Not matched!')


str = input("Enter a String : ")
print(stringmatch(str))

# String "I_am_number_1" matches
# But String "I am number_1" does not matches