#!/usr/bin/python3

import csv
from random import randint

def main():
    print("\nWelcome! Thank you for decising to open your account with us. We will make sure to give you good services and keep your money safe")
    
    CardNum = str()
    for _ in range(12):
        CardNum = CardNum + str(randint(0,9))
    PIN = "0000"
    while True:
        pin = input("Please insert a 4 digits valid PIN: ").strip()
        if (len(pin) == 4):
            PIN = pin
            break
        else:
            print("Invalid input, please try again")
    firstname = input("Please insert your first name: ").strip().upper()
    Lastname = input("Please insert your last name: ").strip().upper()
    balance = 0.0
    print("\nPlease make sure to keep the below information private and secure\n")
    print(f"fullname: {firstname} {Lastname}")
    print(f"PIN: {PIN}")
    print(f"Debitcard number: {CardNum}")
    print(f"current balance: {balance}")
    
    with open("Information.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["CardNum", "PIN", "Firstname", "Lastname", "Balance"])
        writer.writerow({"Firstname": firstname, "Lastname": Lastname, "CardNum": CardNum, "PIN": PIN, "Balance": balance})

if __name__ == "__main__":
    main()

