#!/usr/bin/python3

class Node:

    def __init__(self, data, next_Node=None, prev=None):
        self.data = data
        self.next = next_Node
        self.prev = prev


    def __str__(self):
        return f"({self.data})"

    def __repr__(self):
        return f"Node({self.data})"

class Singly_link_list:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, d):
        newNode = Node(d, self.root)
        self.root = newNode
        self.size += 1
       
    def find(self, d):
        current_Node = self.root
        while current_Node is not None:
            if (current_Node.data == d):
                return d
            else:
                current_Node = current_Node.next
        return False

    def printNode(self):
        while self.root is not None:
            print(self.root, end="->")
            self.root = self.root.next
        print("None")

    def __repr__(self):
        return f"Singly_link_list({self.root})"

def main():
    list = Singly_link_list()
    list.add(5)
    list.add(10)
    list.add(4)
    print(list.find(5))
    list.printNode
    print(list.size)

    print("______________________")

    print(list.find(4))

if __name__ == "main":
    main()

main()
