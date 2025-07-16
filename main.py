# main.py
from bank import Bank

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
