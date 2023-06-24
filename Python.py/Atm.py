#!/usr/bin/python3

import csv
from CardHolder import CardHolder

def Atm():
    def print_menu():
        """Print options to the user"""
        print("\nWelcome to Robert's Atm program")
        print("From the following options, choose one:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        
    def Deposit(CardHolder):
        try:
            deposit = float(input("how much do you want to deposit: "))
            CardHolder.balance = CardHolder.balance + deposit
            #with open("Information.csv", "w") as file:
            #   writer = csv.DictWriter(file, fieldnames=["CardNum", "PIN", "Firstname", "Lastname", "Balance"])
            #  for update in List_of_cardHolders:
            #     writer.writerow({"CardNum": update.cardNum, "PIN": update.pin, "Firstname": update.firstname, "Lastname": update.lastname, "Balance": update.balance})

            print("\nSeccessfully deposited!")
            print(f"Your new balance is {CardHolder.balance}")
        except:
            print("Invalid input")

    def withdraw(CardHolder):
        try:
            Withdraw = float(input("How much do you want to withdraw: "))
            if CardHolder.balance < Withdraw:
                print("\nInsufficient Balance")
            else:
                CardHolder.balance = CardHolder.balance - Withdraw
                print("\nSeccessfully withdraw!")
                print(f"Your new balance is {CardHolder.balance}")
        except:
            print("Invalid input")

    def show_balance(CardHolder):
        print(f"\nMr. {CardHolder.name}, your current balance is: {CardHolder.balance}")
    if __name__ == "__main__":
        current_user = CardHolder("","","","","")

    """ Repo of cardHolder """
    List_of_cardHolders = []

    with open("Information.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            List_of_cardHolders.append(CardHolder(row[0], row[1], row[2], row[3], float(row[4])))

    ## prompt user for debit card number

    debitcardNum = str()
    while True:
        try:
            debitcardNum = input("Please insert your debit card: ").strip()
            debitmatch = [holder for holder in List_of_cardHolders if holder.cardNum == debitcardNum]
            if len(debitmatch) > 0:
                current_user = debitmatch[0]
                break
            else:
                print("Cardnumber not recognized. please try again.")
        except:
            print("Cardnumber not recognized. please try again.")

    ## prompt for pin
    while True:
        try:
            userPIN = input("Please enter a valid PIN: ").strip()
            if current_user.pin == userPIN:
                break
            else:
                print("Invalid PIn. Please try again")
        except:
            print("Invalid PIN, please try again.")

    # print option
    print(f"Welcome Mr. {current_user.name}, :)")
    option = 0
    while True:
        print_menu()
        try:
            option = int(input().strip())
        except:
            print("Invalid input, please try again")

        if option == 1:
            Deposit(current_user)
        elif option == 2:
            withdraw(current_user)
        elif option == 3:
            show_balance(current_user)
        elif option == 4:
            break
        else:
            option = o
    print("Have a nice day. :)")
    with open("Information.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["CardNum", "PIN", "Firstname", "Lastname", "Balance"])
        for update in List_of_cardHolders:
            writer.writerow({"CardNum": update.cardNum, "PIN": update.pin, "Firstname": update.firstname, "Lastname": update.lastname, "Balance": update.balance})


if __name__ == "__main__":
    Atm()
