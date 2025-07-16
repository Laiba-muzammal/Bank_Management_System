# utils.py
import re

def is_valid_password(password):
    if len(password) < 8 or len(password) > 12:
        print("Password length must be between 8 and 12 characters.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not re.search(r"\d", password):
        print("Password must contain at least one digit.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain at least one special character.")
        return False
    return True

def is_valid_contact(contact):
    if not (contact.isdigit() and len(contact) == 11):
        print("Contact number must be 11 digits long.")
        return False
    return True

def is_valid_amount(amount):
    if not amount.isdigit() or int(amount) <= 0:
        print("Invalid amount! Please enter a positive integer.")
        return False
    return True
