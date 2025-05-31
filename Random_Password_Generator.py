import random
import string

def generate_random_password():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer for the password length.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

if __name__ == "__main__":
    generate_random_password()