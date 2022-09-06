import math
import time
from typing import List, Dict, Tuple

from ordliste import Ordbog
import config as conf


class Crypter:
    def __init__(self, key: int = 8) -> None:
        """ The class used to encrypt and decrypt a message """
        self.key = key


    def encrypt(self, msg: str) -> str:
        """ Encrypt a message using the key """
        print(msg)

        out = [] 

        # Find the number of blank trailing spaces using some magical math
        length: int = abs(len(msg) % self.key - self.key)
        rows: int = math.ceil(len(msg) / self.key)

        # Padd the text with replaceable symbols
        msg += "*" * length

        # Loop over each row and create a list containg the chars of each row in the table
        for indx in range(rows):
            out.append(list(msg[indx*self.key : indx*self.key + self.key]))

        # Combine the nested lists
        out = "".join(["".join(i) for i in list(zip(*out))])
        out = out.replace("*", "")

        return out


    def decrypt(self, msg: str) -> str:
        """ Decrypt a message using the key """

        # Find the number of blank trailing spaces using some magical math
        length: int = abs(len(msg) % self.key - self.key)
        rows: int = math.ceil(len(msg) / self.key)

        # Used to keep track of the matrix of letters
        out = [] 

        indx = 0
        multiplier = rows
        # Loop untill the matrix is filled
        while len(out)+1 <= self.key:
            out.append(msg[indx : indx + multiplier])
            
            # If the row is one that held a star earlier
            if len(out) == self.key - length:
                multiplier = rows - 1
                indx += 1

            indx += multiplier

        # Add the padding back to keep track
        # Remove that stars to clean the output
        out = [f"{i}*" if len(i) != len(out[0]) else i for i in out]
        # Zip the matrix together so its normal agein
        out = "".join(["".join(i) for i in list(zip(*out))])
        # Remove that stars to clean the output
        out = out.replace("*", "")

        return out


    def brute(self, msg: str) -> str:
        """ Brute force the Transposition Chiper using a wodlist """

        print(f"Testing {len(msg)-1} keys")
    
        # Dictionarry to keep track of the score of each attempt
        words: Dict[str,Tuple[int,int]] = {}

        # Using a progress bar / meter loop over each posible key
        for i in conf.progressbar(range(1, len(msg))):
            # Encrypt the text
            text = Crypter(i).decrypt(msg)
            score = 0
            # Count up each word and see if its reconised in the wordlist
            for word in text.split(" "):
                score += len(ordbog.search(word))

            # Find the procentage acutacy of the decryption, we compare found words to count of words
            words[text] = (math.ceil(score / (len(text.split(" "))+1) * 100), i)

        words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1][0])} 
        for text, data in words.items():
            print(f"{data[1]} : {data[0]} % - {text}")


ordbog = Ordbog()

crypted = Crypter(69*2).encrypt("Der var en gang en fyr der sage at han gerne ville agere i en verden ude bøvl og larm, dog kom gud og sage at dette ikke ville være en mulighed lige PT, man kan jo også undre sig over hvorfor gud skulle være sådan en lysseslukker? Man skulle jo tro han var brandmand men med elektricitet")
print(crypted)

Crypter().brute(crypted)
