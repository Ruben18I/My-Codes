from numpy import random
import numpy as np

Balance = 0

def Balance_():
    global Balance
    print(f"Your balance: {Balance:.2f}$")

def Withd():
    global Balance
    Amount = float(input("Enter amount to withdraw: $"))
    if Amount <= 0:
        print("Error! Cannot be 0 or negative")
    elif Amount > Balance:
        print("Insufficient funds!")
    else:
        return Amount
    return None

def Dep():
    Amount2 = float(input("Enter amount to deposit: $"))
    if Amount2 <= 0:
        print("Error! Cannot be 0 or negative")
    else:
        return Amount2
    return None

def Gam():
    return np.random.choice(["Heads", "Tails"])

def Gamble(current_balance):
    global Balance
    bet = float(input("Enter bet: $"))
    if bet <= 0:
        print("Invalid bet , Cannot be 0 or negative")
        return
    if bet > Balance:
        print("Insufficient Balance")
        return
    
    choice = input("Choose 1-Heads, 2-Tails: ").strip()
    result = Gam()
    print(f"Coin landed on: {result}")
    
    if (choice == "1" and result == "Heads") or (choice == "2" and result == "Tails"):
        print("Winner!")
        Balance += bet
    else:
        print("Loser!")
        Balance -= bet

def main():
    global Balance
    Run = True
    while Run:
        print("Welcome")
        print("1-Balance, 2-Withdraw, 3-Deposit, 4-Exit, 5-Gamble")
        choice_ = input("Enter choice: ").strip()
        
        if choice_ == "1":
            Balance_()
        elif choice_ == "2":
            amount = Withd()
            if amount is not None:
                Balance -= amount
        elif choice_ == "3":
            amount = Dep()
            if amount is not None:
                Balance += amount
        elif choice_ == "4":
            Run = False
            print("Hagd!")
            break
        elif choice_ == "5":
            Gamble(Balance)
        else:
            print("Not a valid choice")

if __name__ == "__main__":
    main()
