from typing import List, Dict, Tuple, Union

import config as conf

from ordliste import Ordbog

# How often each charecter is seen in the danish alphabeth
frequency = "ERNDTASILGOMKVFHUBPJYCWXZQ"


class Crypter:
    """ Class responsable for handeling decryption"""

    def __init__(self, text) -> None:
        self.text = text
        self.alph = conf.alph
        self.key = {
                "U": "E",
                "T": "A",
                "J": "I",
                "D": "L",
                "E": "R",
                "H": "S",
                "D": "L",
                "E": "R",
                "R": "O",
                "A": "G",
                "X": "V",

                "I": "M",
                "K": "N",
                "Y": "D",
                "B": "T",
                "F": "F",
                "Q": "H",
                "Z": "P",
                "L": "U",
                "V": "B",
                "O": "J",
                "W": "K",
                "S": "Y"
            }
        self.ordbog = Ordbog()

    def get_pattern(self, word: str) -> str:
        """ Create a pattern using the key and unkowen charecters that can be used with ordliste.py """
        out = ""
        letters = {} 
        ltrIndx = 0
        for i in word:
            fnd = self.key.get(i) # The letter found

            if fnd is not None:
                out += fnd
            else:
                if letters.get(i) is not None:
                    out += str(letters.get(i))
                else:
                    letters[i] = ltrIndx
                    out += str(letters.get(i))
                    ltrIndx += 1

        return out

    def preview(self, start: int, stop: int, defaultColor1: str = None, defaultColor2: str = None) -> str:
        """ Show a snippet of the crypted text """
        out = ""

        color1 = conf.F if defaultColor1 is None else defaultColor1
        color2 = conf.B if defaultColor2 is None else defaultColor2

        for i in self.text[start:stop]:
            out += (color1 + self.key.get(i)) if self.key.get(i) is not None else (color2 + i)

        return out

    def preview_sorted(self, acuracy: int = 3) -> Tuple[Tuple,Dict]:
        """ Show all the words and posible corespondanses """
        out = []
        words = []
        parralels: Dict[str,int] = {} # Used to keep track of how often each letter points to anohter letter

        # Loop over each word and check for matches
        for i in sorted(self.text.split(" "), key = len, reverse = True):
            pattern = self.get_pattern(i) # Create the searchable pattern
            found = self.ordbog.search(pattern) # Look for matches
            
            if (len(found) != 0 and # If there is something found 
                    pattern not in words and # Check for dublicates
                    len(found) <= acuracy): # If there are too many matches it beocmes kinda useless
                
                # Find what the letters coresponded to
                for word in found:
                    for ltr1, ltr2 in zip(word, i):
                        
                        # Incerase the cont of that combination eg. EF += 1
                        if parralels.get(f"{ltr2}->{ltr1}") is None:
                            parralels[f"{ltr2}->{ltr1}"] = 1
                        else:
                            parralels[f"{ltr2}->{ltr1}"] += 1

                # Create the letter context preview
                indx = self.text.upper().find(f" {i.upper()} ")
                if indx != -1:
                    context = self.preview(indx - 20, indx + 20 + len(i))
                    context = context.replace(self.preview(indx, indx + len(i) +1), self.preview(indx, indx + len(i) + 1, defaultColor1 = conf.R))
                else:
                    context = "N/A"

                words.append(pattern)
                out.append((i, pattern, found, context))

        # Sort the table and ignore the corralations we already know
        parralels = {k: v for k, v in sorted(parralels.items(), key=lambda item: item[1], reverse = True) if self.key.get(k[0]) != k[-1]}

        return (out, parralels)

    def show_sorted(self):
        """ See likely matches from the encrypted text """
        acuracy = conf.ask("Acuracy (1-5), how restrictive it can be (1 being the most)", parseInt = True)

        matches, letters = self.preview_sorted(acuracy)

        [print(f"{conf.F} {i[0]}: {i[1]} -> {', '.join(i[2]):<10}  ||  {i[3]}  ||") for i in matches]

        print(f"{len(matches)} matches found")
        print("Likely matches:", letters)

    def swap_letter(self, letter: str, arr1: list, arr2: list) -> str:
        """ Swaps a letter with another """
        try:
            # Try to find the index of the letter in the first array
            indx = arr1.index(letter.upper())
        except ValueError: # If the letter / symbol is not found in the array
            return letter 

        return arr2[indx] # Return the letter found in the second array

    def frequency_analasys(self) -> Dict[str,int]:
        """ Run a frequency analasys on the text """
        # Dict to keep track of the letters
        letters = {}
        tot = 0 # Total number of letters

        # Initilaise the dict with default values
        for i in list("ABCDEFGHIJKLMNOPRSTUVWXYZ"):
            letters[i] = 0

        # Loop over the text and increase count for each item
        for i in self.text.upper():
            if letters.get(i) is not None:
                letters[i] += 1
                tot += 1 # Increase the total count of letters

        # Sort the dict by values so its easier to read
        display = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse = True)}

        return display

    def execute_analasys(self) -> None:
        """ Execute a frequency analasys """
        analasys: Dict[str,int] = self.frequency_analasys()

        indx = 0
        for ltr, detections in analasys.items():
            print(f"{conf.F}{ltr}{conf.B} - {conf.F}{detections}{conf.F if indx < 5 else conf.B} {frequency[indx]}")
            indx += 1
