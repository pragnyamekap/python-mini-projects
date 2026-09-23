import random

print("--- PASSWORD GENERATOR ---")

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

length = int(input("Enter password length: "))

all_characters = letters + numbers + symbols

password = ""
for i in range(length):
    password = password + random.choice(all_characters)

print("Your password is:", password)  