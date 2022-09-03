import random

import config as conf

from menu import Menu
from ordliste import Ordbog
from crypto import Crypter

# Load the chiffer text
with open("chiffer.txt", "r") as file:
    data = file.read()

# Initialise the cryptography class
crypter = Crypter(data)
print(crypter.preview(0,900))

# A list of the commands the progam has avaliable
commands = [
        Ordbog().ask_user, # Search for a word
        Crypter(data).show_sorted, # Show the word analasys
        crypter.execute_analasys, # Show a frequency analasys
        conf.safe_exit, # Exit the program
    ]

Menu(commands).menu()

