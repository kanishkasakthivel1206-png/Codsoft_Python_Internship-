# CodeAlpha Python Programming Internship
# Task 3: Password Generator

import secrets
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter the desired password length: "))

        if length < 4:
            print("Password length should be at least 4.")
        else:
            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            break

    except ValueError:
        print("Please enter a valid number.")
