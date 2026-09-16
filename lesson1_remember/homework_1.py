"""
Task 1. Clean a Name
Write a function clean_name(name).
·      Remove spaces from the beginning and end of the string.
·      Return the name in title case.
Example:
print(clean_name("   anna smith   "))
# Anna Smith
print(clean_name("DAVID COHEN"))
# David Cohen
Hint: Think about strip() and title().
"""


s = "  hello world!  "

def clean_name(name):
    return name.strip().title()

print(clean_name(s))

"""
Write a function normalize_email(email).
·      Remove spaces from the beginning and end. 
·      Remove spaces from the beginning and end.
·      Convert all letters to lowercase.
·      Return the cleaned email.
Example:
print(normalize_email("  Anna.Smith@Example.COM  "))
# anna.smith@example.com
Hint: Use strip() and lower().
"""
e = " heleN@test.Com"
def normalize_email(email):
    return email.strip().lower()
print(normalize_email(e))

"""
Write a function is_python_file(filename).
·      Return True if the file name ends with .py.
·      The check must work for .py, .PY, .Py, etc.
Example:
print(is_python_file("lesson.py"))
# True

print(is_python_file("HOMEWORK.PY"))
# True
print(is_python_file("notes.txt"))
# False
Hint: Normalize the case first, then use endswith().
"""

def is_python_file(filename):
    return filename.lower().endswith(".py")

print(is_python_file("license.py"))
print(is_python_file("LESSON.PY"))
print(is_python_file("homework.txt"))

"""
Write a function fix_message(message).
·      Replace every occurrence of the word "bad" with "good".
·      Return the new string.
·      Remember: strings are immutable, so the original string itself is not changed.
Example:
message = "bad weather, bad mood"

result = fix_message(message)

print(result)
# good weather, good mood

print(message)
# bad weather, bad mood
Hint: Use replace().
"""
def fix_message(message):
    return message.replace("bad", "good")

message = "bad weather, bad mood"
result = fix_message(message)
print(result)

"""
def fix_message(message):
    return message.replace("bad", "good")

message = "bad weather, bad mood"
result = fix_message(message)
print(result)
"""

def count_letter(text, letter):
    return text.lower().count(letter.lower())
print(count_letter("abRacaDabra", "a"))

"""
Write a function create_login(first_name, last_name).
·      Remove unnecessary spaces from both names.
·      Convert both names to lowercase.
·      Create a login in the format: first_name.last_name
·      Return the result.
Example:
print(create_login("  Anna ", " SMITH  "))
# anna.smith
Hint: You can combine several string methods in one task.
"""

def create_login(first_name, last_name):
    return first_name.strip().lower() + "." + last_name.strip().lower()

print(create_login(" Helen", " Paltiy"))

"""
Write a function check_password(password). Return True only if all conditions are met:
·      the password has at least 8 characters;
·      it contains no spaces;
·      it is not made only of letters;
print(check_password("python123"))
# True

print(check_password("python"))
# False

print(check_password("python 123"))
# False
Hint: Remember len(), isspace()/the in operator, and isalpha().
"""

def check_password(password):
    return len(password) >= 8 and " " not in password and not password.isalpha()
print(check_password("Helen1983"))
print(check_password("Helen"))
print(check_password(" "))

"""
Write a function split_name(full_name). 
Assume the string contains exactly a first name and a last name separated by spaces.
print(split_name("  Anna   Smith  "))
# ["Anna", "Smith"]
Hint: strip() first, then split().
"""

def split_name(full_name):
    return full_name.strip().split()
print(split_name("Helen Paltiy"))