from cryptography.fernet import Fernet


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


fer = Fernet(load_key())


def view():
    master_password = input("The Password: ")
    if master_password == load_key().decode():
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                platform, user, passw = data.split("|")
                print(platform, ", User:", fer.decrypt(user.encode()).decode(),
                      ", Password:", fer.decrypt(passw.encode()).decode())
    else:
        print("WRONG! Lord Voldemort and his Death eaters are after you (you better run) :P")
