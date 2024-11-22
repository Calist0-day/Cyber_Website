import string
import secrets


def generate_password(length, numbers, symbols):
    if length > 50:
        return "Password too long"
    password = ""
    characters = string.ascii_letters
    if (numbers):
        characters += string.digits
    if (symbols):
        characters += string.punctuation
    for i in range(length):
        password += secrets.choice(characters)

    return password

