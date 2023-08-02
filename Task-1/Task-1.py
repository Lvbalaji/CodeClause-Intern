import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Change this value to set the desired password length
    password = generate_random_password(password_length)
    print("Generated Password:", password)
