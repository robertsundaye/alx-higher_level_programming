#!/usr/bin/python3

def main():
    name = get_name()
    print(f"hello {name}")

def get_name():
    return input("Pleast eneter your name: ").strip()

if __name__ == "__main__":
    main()
