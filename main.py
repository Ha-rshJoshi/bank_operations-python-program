min_bal=0
balance=0
account={}

def account_open():
    global balance
    name = input("Enter customer name: ")
    account_no = input("Enter account number: ")
    balance = float(input("Enter balance: "))
    account["name"] = name
    account["account_no"] = account_no
    print("Account opened successfully")

def deposit():
    global balance
    amt=float(input("Enter amount to deposit: "))
    balance += amt
    print("Amount deposited successfully")
    print("Current balance is: ", balance)

def withdraw():
    global balance
    amt=float(input("Enter amount to withdraw: "))
    if balance-amt<min_bal:
        print("Not enough money in the account")
    else:
        balance -= amt
        print("Amount withdrawn successfully")
        print("Current balance is: ", balance)

def fixed_deposit():
    global balance
    amt=float(input("Enter FD amount : "))
    year=int(input("Enter period (years) : "))
    s=input("Are you senior citizen or not (Y/N) :")
    if year<1:
        rate=5
    elif year<=3:
        rate=6
    else:
        rate=7
    if s=="Y":
        rate=rate+0.5
    maturity=amt+(amt*rate*year)/100
    print("Interest rate is: ", rate)
    print("Maturity amount is: ", maturity)

while True:
    print("------BANK MENU------")
    print("1. Open Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Fixed Deposit Money")
    print("5. Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        account_open()
    elif choice==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        fixed_deposit()
    elif choice==5:
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid choice")