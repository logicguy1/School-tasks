"""

Task: Create a dictionarry where you can store, modify and remove words and explanation
You should also make the program able to save using pickle

"""

import colored
import pickle
import sys
import os

## Initialise color variables
R = colored.fg("#707070")
F = colored.fg("#ee4665")
E = colored.fg("#e0e0e0")

# Function to clear the screen, cross platform
clear = lambda : os.system('cls' if os.name == 'nt' else 'clear')

class Dictionarry:
    def __init__(self, data):
        self.words = data

    def __len__(self) -> int:
        """ Get the amount of words in the dictionarry """
        return len(self.words)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self) -> list:
        if self.n < len(self):
            item = list(self.words.items())[self.n]
            self.n += 1

            return item
        else:
            raise StopIteration


    def get(self, word:str) -> dict:
        """ Finds a word in the dictionarry """

        out = {} 

        for term, explanation in self:
            if word.upper() in term.upper():
                out[term] = explanation

        return out

    def add_word(self) -> bool:
        """ Tilføj et ord """

        word = input(f"{E}Ordet du gerne vil tilføje\n{R}>>{F} ")
        explanation = input(f"{E}En forklaing af ordet\n{R}>>{F} ")

        self.words[word] = explanation
        return False

    def show_words(self, words:dict, lineNumbers:bool = False) -> None:
        """ Vis ord i en pæn liste """

        if len(words) == 0: return

        maxLenght = len(max(words, key=len))
        indx = 0
        
        for term, explanation in words.items():
            indx += 1
            lineNum = f"{F}{indx}. " if lineNumbers else ""

            print(f"{lineNum}{E}{term.capitalize() :<{maxLenght}}{R}:{E} {explanation.capitalize()}")

    def display_words(self) -> bool:
        """ Vis ord """
 
        self.show_words(self.get(""))
        return True

    def show_word(self) -> bool:
        """ Søg efter ord """

        prompt = input(f"{E}Hvad vil du søge efter\n{R}>>{F} ")
        result = self.get(prompt)
        self.show_words(result)

        return True

    def remove_word(self) -> bool:
        """ Fjærn ord """

        self.show_words(self.words, lineNumbers = True)

        indx = input(f"\n{E}Hvilken ord vil du slette? (index)\n{R}>>{F} ")
        key = list(self.words.keys())[int(indx) - 1]
        del self.words[key]

        return False

    def modify_word(self) -> bool:
        """ Ændre på et ord """

        self.show_words(self.words, lineNumbers = True)

        indx = input(f"\n{E}Hvilken ord vil du redigere? (index)\n{R}>>{F} ")
        key = list(self.words.keys())[int(indx) - 1]

        
        


def menu():
    try:
        data = pickle.load(open("save.p", "rb"))
    except (EOFError, FileNotFoundError):
        data = {}

    myDict = Dictionarry(data)

    def safe_exit():
        """ Forlad programmet og gem"""

        pickle.dump(myDict.words, open("save.p", "wb"))
        print(f"Done{E}")

        sys.exit(0) # Exit without errors

    choices = [myDict.display_words,
               myDict.add_word,
               myDict.show_word,
               myDict.remove_word,
               safe_exit]

    while True:
        clear()

        # Tell the user their choices
        for choice, i in zip(choices, range(1, len(choices) + 1)):
            print(f"{F}{i}{R}:{E} {choice.__doc__.strip()}")

        choice = input(f"\n{R}>>{F} ")
        print()

        if not choice.isdigit():
            input(f"{E}Skal være et tal!\n\n{R}Tryk enter for at komme videre.")
            continue

        func = choices[int(choice) - 1]

        ask = func() # Returns true if the user should be prompted to pass
        if ask: input(f"\n{R}Tryk enter for at komme videre.")
        

if __name__ == "__main__":
    menu()

