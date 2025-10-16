import random, string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
