import random
import string


def generate_password(length, have_digits, have_punctuation):
    password = ""
    characters = string.ascii_letters
    if have_digits:
        characters += string.digits
    if have_punctuation:
        characters += string.punctuation
    for _ in range(length):
        char = random.choice(characters)
        password += char
    return password
