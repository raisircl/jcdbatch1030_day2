from bankacc import BankAcc
accounts=[]
while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial balance: "))
        account = BankAcc(name, initial_balance)
        accounts.append(account)
        print(f"Account created successfully! Account Number: {account.acc_no}")

    elif choice == '2':
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        for account in accounts:
            if account.acc_no == acc_no:
                account.deposit(amount)
                break
        else:
            print("Account not found.")

    elif choice == '3':
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        for account in accounts:
            if account.acc_no == acc_no:
                account.withdraw(amount)
                break
        else:
            print("Account not found.")

    elif choice == '4':
        acc_no = int(input("Enter account number: "))
        for account in accounts:
            if account.acc_no == acc_no:
                balance = account.get_balance()
                print(f"Current balance is {balance}.")
                break
        else:
            print("Account not found.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")