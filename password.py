import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set (uppercase, lowercase, numbers, special characters) must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    length = int(input("Enter the desired password length: "))
    count = int(input("Enter the number of passwords to generate: "))

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    for _ in range(count):
        password = generate_password(length, uppercase, lowercase, numbers, special_chars)
        if password:
            print("Generated Password:", password)

if __name__ == "_main_":
    main()