# account.py
from datetime import datetime
from utils import is_valid_amount

class Account:
    def __init__(self):
        self.users = {}
        self.transactions = []

    def authenticate_user(self):
        user_name = input("Enter your username: ")
        user = self.users.get(user_name)
        
        if not user:
            print("Invalid username!")
            return None
        
        password = input("Enter your password: ")
        if user.password != password:
            print("Invalid password!")
            return None
        
        print("Login successful!")
        return user

    def deposit(self, user):
        while True:
            amount = input("Enter the amount you want to deposit: (positive integer) ")
            if not is_valid_amount(amount):
                continue
            
            amount = int(amount)
            user.balance += amount
            
            self.transactions.append({
                'type': 'deposit',
                'amount': amount,
                'balance_after': user.balance,
                'user_name': user.username,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print("Transaction Successful!")
            break

    def withdraw(self, user):
        retries = 3
        while retries > 0:
            amount = input("Enter the amount you want to withdraw: (positive integer) ")
            if not is_valid_amount(amount):
                retries -= 1
                continue

            amount = int(amount)
            if amount > user.balance:
                print(f"Insufficient balance! You have only {user.balance}.")
                retries -= 1
                retry = input(f"Do you want to try again? ({retries} attempts left) (yes/no): ").lower()
                if retry != 'yes':
                    break
                continue

            user.balance -= amount

            self.transactions.append({
                'type': 'withdraw',
                'amount': amount,
                'balance_after': user.balance,
                'user_name': user.username,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            print("Transaction Successful!")
            break
        else:
            print("Too many failed attempts. Exiting withdrawal process.")
