import re
from datetime import datetime

class User:
    def __init__(self, username, name, password, balance=0, contact=None, address=None):
        self.username = username  
        self.name = name          
        self.balance = balance    
        self.password = password  
        self.contact = contact    
        self.address = address    

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
            if not self.is_valid_amount(amount):  
                print("Invalid amount! Please try again.")
                continue  
            
            amount = int(amount)
            user.balance += amount  
            
            transaction_record = {
                'type': 'deposit',
                'amount': amount,
                'balance_after': user.balance,
                'user_name': user.username,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
            }
            
            self.transactions.append(transaction_record)  
            print("Transaction Successful!")
            break  

    def withdraw(self, user):
        retries = 3  
        while retries > 0:  
            amount = input("Enter the amount you want to withdraw: (positive integer) ")
            if not self.is_valid_amount(amount):  
                print("Invalid amount! Please try again.")
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

            transaction_record = {
                'type': 'withdraw',
                'amount': amount,
                'balance_after': user.balance,
                'user_name': user.username,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
            }
            
            self.transactions.append(transaction_record)  
            print("Transaction Successful!")
            break  
        else:
            print("Too many failed attempts. Exiting withdrawal process.")

    def is_valid_amount(self, amount):
        if not amount.isdigit() or int(amount) <= 0:  
            print("Invalid amount! Please enter a positive integer.")
            return False
        return True  

class Bank:
    def __init__(self):
        self.account = Account()  

    def register(self):
        while True:  
            username = input("Enter a username for your account: ")

            if username in self.account.users:  
                print("Username already exists. Please choose another username.")
                continue  

            while True:
                name = input("Enter your name: ")
                if not name.isalpha():
                    print("Name must contain only alphabets. Please try again.")
                    continue
                break

            while True:
                password = input("Enter a password for your account (8-12 characters, must include an uppercase letter, a lowercase letter, a digit, and a special character): ")
                if not self.is_valid_password(password):  
                    print("Invalid password. Please try again.")
                    retry = input("Do you want to try again? (yes/no): ").lower()
                    if retry != 'yes':
                        return  
                    continue  
                break  

            while True:
                contact = input("Enter your contact number (11 digits): ")
                if not self.is_valid_contact(contact):  
                    print("Invalid contact number. Please try again.")
                    retry = input("Do you want to try again? (yes/no): ").lower()
                    if retry != 'yes':
                        return
                    continue  
                break  
              
            while True:
                address = input("Enter your address: ")
                if not address:  
                    print("Address is mandatory, please fill it.")
                    retry = input("Do you want to try again? (yes/no): ").lower()
                    if retry != 'yes':
                        return  
                    continue  
                break  
              
            new_user = User(username, name, password, 0, contact, address)  
            self.account.users[username] = new_user  
            print("Registered Successfully!")
            return  

    def is_valid_password(self, password):
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

    def is_valid_contact(self, contact):
        if not (contact.isdigit() and len(contact) == 11):  
            print("Contact number must be 11 digits long.")
            return False
        return True  

    def login(self):
        user = self.account.authenticate_user()  
        if user:
            return user  
        return None  

    def check_bal(self, user):
        print(f"Your balance is: {user.balance}")        

    def view_transaction(self, user):
        user_transactions = [trans for trans in self.account.transactions if trans['user_name'] == user.username]  
        if not user_transactions:  
            print("No transaction records found!")
            return
        
        print("Your recent transactions are as follows:")  
        for transaction in user_transactions:  
            print(f"{transaction['type'].capitalize()} of amount {transaction['amount']} at {transaction['timestamp']}, New balance: {transaction['balance_after']}")

bank = Bank()  
user = None  

while True:
    print("\nWELCOME TO OUR BANK \n***MENU*** ")
    print("1. Register an account\n2. Login to your account\n3. Deposit money\n4. Withdraw money\n5. Check your balance\n6. View Transaction History\n7. Exit")
    
    try:
        opt = int(input("Kindly enter your option: "))  
    except ValueError:  
        print("Invalid option. Please enter a number.")  
        continue

    match opt:  
        case 1:  
            bank.register() 
        case 2:  
            user = bank.login()  
        case 3:  
            if user:
                bank.account.deposit(user)   
            else:
                print("You need to log in first.")
        case 4:  
            if user:
                bank.account.withdraw(user)  
            else:
                print("You need to log in first.")
        case 5:  
            if user:
                bank.check_bal(user)  
            else:
                print("You need to log in first.")
        case 6:  
            if user:
                bank.view_transaction(user)  
            else:
                print("You need to log in first.")
        case 7:  
            print("Thanks for using our services...See you soon!")  
            break  
        case _:  
            print("Invalid option....Please enter relevant option")
