
import config as conf

class Crypter:
    def __init__(self, text) -> None:
        self.text = text
        self.alph = conf.alph
        self.key = {}

    def swap_letter(self, letter: str, arr1: list, arr2: list) -> str:
        """ Swaps a letter with another """
        try:
            indx = arr1.index(letter.upper())
        except ValueError:
            return letter 

        return arr2[indx]
