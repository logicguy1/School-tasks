import random

class Key:
    """ Create a key from small passphrase """
    def __init__(self, passwd:str = "") -> None:
        self.raw = list("ABCDEFGHIJKLMNOPRSTUVWXYZÆØÅ")
        self.key = list("ABCDEFGHIJKLMNOPRSTUVWXYZÆØÅ")
        
        random.seed(passwd) # Set the seed with random so we always get the same key from the passphrase

        for i in range(5):
            random.shuffle(self.key)


class Ceasar:
    """ Handle the cryptographic part of algarythem """
    def __init__(self, key: Key, shift: int = 1) -> None:
        """ key: KeyObject, shift: amount to shift (int) """
        self.myKey = key
        self.shift = shift

    def swap_letter(self, letter: str, arr1: list, arr2: list) -> str:
        """ Swaps a letter with another """
        try:
            indx = arr1.index(letter.upper())
        except ValueError:
            return letter 

        return arr2[indx]

    def encrypt(self, phrase:str) -> str:
        """ Encrypt a message using the key """
        txt = "".join([self.swap_letter(i, self.myKey.key, self.myKey.raw) for i in phrase])
        return txt

    def decrypt(self, phrase:str) -> str:
        """ Decrypt a message using the key """
        txt = "".join([self.swap_letter(i, self.myKey.raw, self.myKey.key) for i in phrase])
        return txt



if __name__ == "__main__":
    myKey = Key("passwdei23")
    print(myKey.key)
    crypt = Ceasar(myKey, 8)

    with open("chiffer.txt", "r") as file:
        chiffer = crypt.encrypt(file.read())

    with open("chiffer.txt", "w") as file:
        file.write(chiffer)

    inp = input("String: ")
    print("en", crypt.encrypt(inp))
    print("de", crypt.decrypt(inp))
