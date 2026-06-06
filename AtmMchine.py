#من مجموعة : رعد محمد , عبدالله القثامي , يوسف العمري

#Defining FUNCTIONS By "def"
def show_Balance(balance):
    print("*********************")
    print(f"Your balance is {balance:.2f}$")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter your depositable amount: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("Error: Amount can't be less than 0")
        print("*********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter Amount to withdraw: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be over 0!")
        print("*********************")
        return 0
    else:
        return amount

#حساب بنكي من الصفر

balance = 0
is_running = True

  #خيارات الة الصرافة Arrays
while is_running:
    print("*********************")
    print("ATM MACHINE")
    print("*********************")
    print("1:Show Balance")
    print("2:Deposit")
    print("3:Withdraw")
    print("4:Exit")

    choice = input("Enter your choice from 1 to 4 : ")

#Using the "if" Statement right here
    if choice == '1':
        show_Balance(balance)
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw(balance)
    elif choice == '4':
        is_running = False
    else:
        #if choosen a non-existant choice

        print("Error : This is not a choice in list" \
        " Please try again")
        print("*********************")


print("Have a nice day!")

        #And Yes, This code is running in loops 