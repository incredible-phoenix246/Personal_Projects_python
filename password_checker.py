# Ask the user to enter a password
password = input("Enter a password: ")

# Initialize variables to check criteria
has_upper = False
has_lower = False
has_digit = False
has_special = False

# Define a set of special characters
special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

# Check password criteria
if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

# Check if all criteria are met
if has_upper and has_lower and has_digit and has_special:
    print("Password is valid.")
else:
    print("Password is not valid. Make sure it has at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.")
