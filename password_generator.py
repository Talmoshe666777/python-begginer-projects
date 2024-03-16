import random
import string

def generate_pass(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    chars = letters
    if numbers:
        chars += digits
    if special_chars:
        chars += special

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(chars)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd


pass_length = int(input("Enter password length: "))
has_number = input("Do you want to have numbers? (y/n)").lower() == "y"
has_special = input("Do you want to have special characters? (y/n)").lower() == "y"
pwd = generate_pass(pass_length, has_number, has_special)
print(pwd)
