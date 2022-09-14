from typing import List, Dict, Set

import config as conf

import csv

class Ordbog:
    def __init__(self) -> None:
        self.words: Set[str] = {} 

    def search(self, pattern: str) -> List[str]:
        """ Search for a word, (__llo) """
        pattern = pattern.upper()

        # Get only the words that is the same length as the pattern
        words: List[str] = [i for i in self.words if len(i) == len(pattern)]
        found: List[str] = [] # List used for the words matching the search 

        for word in words:
            # Should we append the word to the list? Will be True if no missmatch is found
            success = True
            ltrIndx = 0
            letters: Dict[str,int] = {} # Taken letters in the word

            # Loop over each letter and check if it matches the case
            for ltr, indx in zip(word, range(len(pattern))):
                if ltr == pattern[indx] or pattern[indx] == "_":
                    continue

                if letters.get(ltr) is not None:
                    if pattern[indx] == str(letters.get(ltr)):
                        continue
                    else:
                        success = False
                else:
                    letters[ltr] = ltrIndx
                    if pattern[indx] == str(letters.get(ltr)):
                        pass
                    else:
                        success = False
                    ltrIndx += 1

            if success:
                found.append(word)

        return found


    def quick_search(self, word: str) -> bool:
        """ Search for exact matches in the wordlist """
        return word.upper() in self.words

                
    def ask_user(self) -> None:
        """ Lookup a word in the database """

        resp: str = conf.ask("Pattern to search for (MA_G_)")
        found = self.search(resp)

        # If none were found
        if len(found) == 0:
            return ""

        # Display what was found and where the charecters were found
        out = ""
        for word, indx in zip(found, range(len(found))):
            out += f"{conf.R}{indx}. "
            # Loop over found and response and add them to out
            for fnd, rsp in zip(word, resp):
                if rsp == "_":
                    out += conf.B + fnd
                else:
                    out += conf.F + fnd
            
            # Add a comma between each item
            out += conf.F + ", " 

        out = out[:-2] # Remove trailing ", "

        print(out, end = "\n\n")


    def load_file(self, path:str) -> None:
        """ Load a file with eacher word split by a newline """
        with open(path, "r") as file:
            data = [i.strip() for i in file.readlines()]

        self.words = set(data)

    def load_csv(self, path:str) -> None:
        with open(path, "r") as file:
            reader = csv.reader(file, delimiter=";")
            data = [i[0].strip().upper() for i in reader]

        self.words = set(data)



if __name__ == "__main__":
    ordbog = Ordbog()
    ordbog.ask_user()
    # print(conf.R + str(ordbog.search("__E_")))



