# models.py
class User:
    def __init__(self, username, name, password, balance=0, contact=None, address=None):
        self.username = username
        self.name = name
        self.balance = balance
        self.password = password
        self.contact = contact
        self.address = address
