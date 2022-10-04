import config as conf


class Crypt:
    def __init__(self, key: str) -> None:
        self.key = key.upper()

    def swap_ltr(self, ltr1: str, ltr2: str, multiplier: int = 1) -> str:
        """ Swap a letter corosponding to the key """

        # Generate the shift ratio
        try:
            ltrIndx = conf.alph.index(ltr1)
            shift = conf.alph.index(ltr2) * multiplier
        except ValueError:
            return ltr1

        # Shift the alphabeth
        alph = conf.alph + conf.alph + conf.alph
        alph = alph[shift+len(conf.alph):shift+len(conf.alph)*2]

        # Return the result
        return alph[ltrIndx]
    
    def encrypt(self, text):
        keyIndx = 0
        out = ""

        for ltr in text.upper():
            out += self.swap_ltr(ltr, self.key[keyIndx % len(self.key)], 1)
            keyIndx += 1

        return out

    def decrypt(self, text):
        keyIndx = 0
        out = ""

        for ltr in text.upper():
            out += self.swap_ltr(ltr, self.key[keyIndx % len(self.key)], -1)
            keyIndx += 1

        return out

if __name__ == "__main__":
    print(Crypt("HELLO").swap_ltr("F", "B"))
    print(Crypt("HELLO").encrypt("GOODAY SON HOW ARE YOU???!"))
    print(Crypt("HELLO").decrypt("NTÆOOC AÆÅ LÆE HVP JWY???!"))

