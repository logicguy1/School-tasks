import random

import config as conf

from menu import Menu
from ordliste import Ordbog
from cryptoo import Crypter

with open("chiffer.txt", "r") as file:
    data = file.read()

crypter = Crypter(data)

commands = [
        Ordbog().ask_user,
        conf.safe_exit
    ]

if __name__ == "__main__":
    pass

