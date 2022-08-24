import random

class Key:
    """ Create a key from small passphrase """
    def __init__(self, passwd:str = "") -> None:
        self.raw = list("ABCDEFGHIJKLMNOPRSTUVWXYZÆØÅ")
        
        random.seed(passwd) # Set the seed with random so we always get the same key from the passphrase
        self.key = self.raw

        for i in range(5):
            random.shuffle(self.key)

class Ceasar:
    """ Handle the cryptographic part of algarythem """
    def __init__(self, key: Key, shift: int = 1) -> None:
        """ key: KeyObject, shift: amount to shift (int) """
        self.myKey = key
        self.shift = shift

    def swap_letter(self, letter: str, shift: int) -> str:
        """ Swaps a letter with another """
        try:
            indx = self.myKey.key.index(letter.upper())
        except ValueError:
            return letter 

        return self.myKey.key[(indx + shift) % len(self.myKey.key)]

    def encrypt(self, phrase:str) -> str:
        """ Encrypt a message using the key """
        txt = "".join([self.swap_letter(i, self.shift) for i in phrase])
        return txt

    def decrypt(self, phrase:str) -> str:
        """ Decrypt a message using the key """
        txt = "".join([self.swap_letter(i, self.shift * -1) for i in phrase])
        return txt



if __name__ == "__main__":
    myKey = Key("passwdei23")
    print(myKey.key)
    crypt = Ceasar(myKey, 8)

    # with open("chiffer.txt", "r") as file:
    #     print(crypt.decrypt(file.read()))

    inp = input("String: ")
    print(crypt.encrypt(inp))
    print(crypt.decrypt(inp))
