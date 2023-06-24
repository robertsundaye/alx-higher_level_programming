#!/usr/bin/python3

class CardHolder:
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.name = f"{self.firstname} {self.lastname}"

    ## getter 
    @property
    def cardNum(self):
        return self.__cardNum
    @property
    def pin(self):
        return self.__pin
    @property
    def firstname(self):
        return self.__firstname
    @property
    def lastname(self):
        return self.__lastname
    @property
    def balance(self):
        return self.__balance

    ## setters
    @cardNum.setter
    def cardNum(self, value):
        self.__cardNum = value
    @pin.setter
    def pin(self, value):
        self.__pin = value
    @firstname.setter
    def firstname(self, value):
        self.__firstname = value
    @lastname.setter
    def lastname(self, value):
        self.__lastname = value
    @balance.setter
    def balance(self, value):
        self.__balance = value

    ## print information
    @property
    def printinfor(self):
        print(f"card num: {self.__cardNum}")
        print(f"Pin num: {self.__pin}")
        print(f"Full name: {self.__firstname} {self.__lastname}")
        print(f"balance: {self.__balance}")
