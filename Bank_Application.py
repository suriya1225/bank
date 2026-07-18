class Bank:
    account_list = {}
    bank_name = "               FITA BANK"
    
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    
    def create_account():
        print("-"*40)
        acc_no = input("Enter Your Account No.       : ")
        name = input("Enter Your Name              : ")
        balance = int(input("Enter your Initial payment   : "))
        print("-"*40)
        account = Bank(acc_no,name,balance)
        Bank.account_list[acc_no] = account 
        print(f"{name} Account Created Successfully....")
        
    def deposit():
        try:
            acc_no  = input("Enter a Account no.     : ")
            if acc_no not  in Bank.account_list:
                raise Exception("ACCOUNT IS NOT FOUNDED")
            amount = int(input("Enter a Deposit Amount  : "))
            if amount < 0:
                raise Exception("PLEASE ENTER YOUR AMOUNT CORRECTLY")
            Bank.account_list[acc_no].balance += amount
            print("="*40)
            print(Bank.bank_name)
            print("="*40)
            print(f"Account No.    : {acc_no}")
            print(f"Account Holder :  {Bank.account_list[acc_no].name}")
            print(f"{amount} is Successfully Deposited.........")
            print("="*40)
        except Exception as e:
            print(f"Error : {e}")
            
    def withdraw():
        try:
            acc_no = input("Enter a Account.No      : ")
            if acc_no not in Bank.account_list:
                raise Exception("Account is not Found")
            account = Bank.account_list[acc_no]
            amount = int(input("Enter a Withdraw Amount : "))
            if amount < 0:
                raise Exception("PLEASE ENTER YOUR AMOUNT CORRECTLY")
            account.balance -= amount
            
            print("="*40)
            print(Bank.bank_name)
            print("="*40)
            print(f"Account no.    : {acc_no}")
            print(f"Account Holder : {Bank.account_list[acc_no].name} ")
            print(f"{amount} amount is Successfully Withdraw.......")
            print("="*40)
            
        except Exception as e:
            print(f"Error: {e}")
    
    def show_balance():
        try:
            acc_no = input("Enter a Account No. : ")
            if acc_no not in Bank.account_list:
                raise Exception("ACCOUNT IS NOT FOUNDED")
            
            print("="*40)
            print(Bank.bank_name)
            print("="*40)
            print(f"Account Holder : {Bank.account_list[acc_no].name}")
            print(f"balance        : {Bank.account_list[acc_no].balance}")
            print("="*40)
            
        except Exception as e:
            print(f"Error: {e}")
        
while True:
    print("="*40)
    print(Bank.bank_name)
    print("="*40)
    print("1. Create Bank Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. show balance")
    print("="*40)
    
    choice = input("Enter Your Choice(1/2/3/4): ")
    
    if choice == "1":
        Bank.create_account()
    elif choice == "2":
        Bank.deposit()
    elif choice == "3":
        Bank.withdraw()
    elif choice == "4":
        Bank.show_balance()
    else:
        print("Invalid Choice")
    