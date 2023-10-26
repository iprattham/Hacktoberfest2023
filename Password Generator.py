# Password Generator - Python Program
import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Check if the length is valid
    if length < 4:
        return "Password length should be at least 4 characters."
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for the password length.")
