from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from encrypt import add
from decrypt import view
import os
import base64


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


def derive_key(passphrase):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=load_key(),
        iterations=480000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passphrase))


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


while True:
    mode = input("Would you like to add a new password or view existing ones? type view/add or q to quit: ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
