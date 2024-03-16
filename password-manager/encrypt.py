from cryptography.fernet import Fernet


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


fer = Fernet(load_key())


def add():
    platform = input('Platform: ')
    user_name = input('User Name: ')
    pwd = input("Password: ")

    # ith remove the need to close the file
    # Example without with:
    # file = open('password.txt', 'a')
    # file.close()
    # open(file name, mode) -> some modes: w=write(use to override), r=read, a=allow to add something to the end of the
    # file and check if file exists(if not it creates it)
    with open('password.txt', 'a') as f:
        f.write(platform + "|" + fer.encrypt(user_name.encode()).decode() +
                "|" + fer.encrypt(pwd.encode()).decode() + "\n")
