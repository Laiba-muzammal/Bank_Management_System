# bank.py
from models import User
from utils import is_valid_password, is_valid_contact
from account import Account

class Bank:
    def __init__(self):
        self.account = Account()

    def register(self):
        while True:
            username = input("Enter a username for your account: ")
            if username in self.account.users:
                print("Username already exists. Please choose another.")
                continue

            name = input("Enter your name: ")
            if not name.isalpha():
                print("Name must contain only alphabets.")
                continue

            password = input("Enter a secure password: ")
            if not is_valid_password(password):
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry != 'yes':
                    return
                continue

            contact = input("Enter your contact number (11 digits): ")
            if not is_valid_contact(contact):
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry != 'yes':
                    return
                continue

            address = input("Enter your address: ")
            if not address:
                retry = input("Do you want to try again? (yes/no): ").lower()
                if retry != 'yes':
                    return
                continue

            new_user = User(username, name, password, 0, contact, address)
            self.account.users[username] = new_user
            print("Registered Successfully!")
            return

    def login(self):
        return self.account.authenticate_user()

    def check_bal(self, user):
        print(f"Your balance is: {user.balance}")

    def view_transaction(self, user):
        transactions = [
            t for t in self.account.transactions if t['user_name'] == user.username
        ]
        if not transactions:
            print("No transaction records found!")
            return
        print("Your transactions:")
        for t in transactions:
            print(f"{t['type'].capitalize()} of {t['amount']} at {t['timestamp']}, New balance: {t['balance_after']}")
