from cryptography.fernet import Fernet
import time
import random
import string

master_pwd = input("Enter Master password: ")

'''(only used once)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()''' 


def load_key():
    with open("key.key" , "rb") as f:
        key = f.read()
        return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        

def randompass():
    n = int(input("Enter length for random password: "))
    passwd = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    print("The generated random password : " + str(passwd))
    

def false_view():
    with open('pseudo_passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=11))
            print("User:", res, "| Password:", passw + res)


def false_add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('pseudo_passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


if(master_pwd == "admin"):
    while True:
        print("Add a new password (add) / View existing passwords (view)")
        print("Random password generator(random) / Quit the program (q): ")
        mode = input()
        if mode == "q":
            print("Quitting program in 3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "random":
            randompass()
        else:
            print("Invalid mode.")
            continue
else:
    while True:
        print("Add a new password (add) / View existing passwords (view)")
        print("Random password generator(random) / Quit the program (q): ")
        mode = input()
        if mode == "q":
            print("Quitting program in 3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
        if mode == "view":
            false_view()
        elif mode == "add":
            false_add()
        elif mode == "random":
            randompass()
        else:
            print("Invalid mode.")
            continue
