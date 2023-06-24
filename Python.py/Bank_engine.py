#!/usr/bin/python3

import cmd
from Account import main
from Atm import Atm

class Bank(cmd.Cmd):
    prompt = '>>>'

    def do_Create_Account(self, arg):
        main()

    def do_ATM_Service(self, arg):
        print("Welcome to the ATM Service")
        print("Please enter the below information to get started")
        Atm()

    def do_quit(self, arg):
        print("Quitting....")
        return True

if __name__ == "__main__":
    Bank().cmdloop()
