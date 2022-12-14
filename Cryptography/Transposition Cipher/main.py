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
            time.sleep(0.005)
            
            # Encrypt the text
            text = Crypter(i).decrypt(msg)
            score = 0
            # Count up each word and see if its reconised in the wordlist
            for word in text.split(" "):
                # score += len(ordbog.search(word))
                score += int(ordbog.quick_search(word))

            words[text] = (score, i)
            
        words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1][0])} 
        for text, data in words.items():
            print(f"{conf.R}{data[1]:>4} {conf.B}:{conf.F} {text} {conf.B}-{conf.F} {round(data[0] / text.count(' ') * 100)} % ")


if __name__ == "__main__":
    ordbog = Ordbog()
    # ordbog.load_file("ordliste.txt")
    ordbog.load_csv("ordliste.csv")

    #crypted = Crypter(5).encrypt(r"""Der var en gang en fyr der sage at han gerne ville agere i en verden ude b??vl og larm, dog kom gud og sage at dette ikke ville v??re en mulighed lige PT, man kan jo ogs?? undre sig over hvorfor gud skulle v??re s??dan en lysseslukker? Man skulle jo tro han var brandmand men med elektricitet Lydsystemet for dansk har et rigt vokalinventar, hvor der skelnes mellem 16-18 forskellige vokalkvaliteter. Desuden skelnes der mellem korte, lange og st??dte vokaler. Ogs?? konsonanterne har deres variation, og de danske konsonanter sv??kkes i stavelsesfinal position. Det g??r, at der findes flere s??kaldt vokoide konsonanter som i fx mad ~ ma??, hav ~ hau og mor ~ mo??. Det tryksvage e, schwa, smelter ofte sammen med nabolyde (schwa-assimilation) som derved bliver stavelsesb??rende. Den danske udtale kan v??re sv??r at h??ndtere for udl??ndinge. Velkendt er r??dgr??d med fl??de, en uklar gr??nse mellem vokaler og konsonanter som skaber lange vokaliske sekvenser, ligesom i r??get ??rred. De danske dialekter har ??t, to eller tre grammatiske k??n, og kendeordet kan v??re efterh??ngt eller foranstillet. P?? F??r??erne findes den s??rlige skriftsprogsn??re udtaleform g??tudansk, i Sydslesvig sydslesvigdansk. De traditionelle dialekter er p?? retur og erstattes efterh??nden af et landsd??kkende rigsdansk, men udtalen varierer stadig i landets egne. Et kendetegn ved det vestjyske er st??d, mens specielt sproget p?? Fyn, Lolland og Falster samt p?? Bornholm synes at ligne mere (d)et syngende svensk(e). S??ledes har nogle syddanske dialekter musikalsk accent. Socialt betingede udtaleforskelle, sociolekter, er (eller var engang) mest velkendt fra K??benhavneromr??det ??? det borgerlige h??jk??benhavnske, senere rigsdansk, og arbejderklassens lavk??benhavnske, gadesproget. Sprogf??llesskaber markeres af en genkendelig sprogform, det v??re sig i udtale eller grammatik, og medlemmer fra andre sprogf??llesskaber end det danske kan s?? b??re disse kendem??rker med i deres danske sprogudtale, og det kaldes ogs?? en etnolekt. Det h??rer alt sammen med til det levende sprog. Dansk p??virker ogs?? andre sprog. S??ledes findes der danske p??virkninger i de nordfrisiske dialekter i Sydslesvig (f. eks. ej og ikke ??? ai p?? Mooring, ei i Fering og ????mrang og ek p?? S??lring, dreng ??? dring p?? Fering, ????mrang og Mooring og dreeng p?? S??lring; ild ??? ial p?? F??r og Amrum, iilj i B??kingherred)[10][11]. Da Gotland var dansk i ??rene 1361 til 1645 kom der ogs?? mange danske l??neord ind i gutam??let (gutnisk). Eksempler. som findes endnu i dag, er n??gle (dansk nogle, svensk n??gra), saktens (dansk sagtens, svensk nog visst) eller um en trent (dansk omtrent, svensk ungef??r)[12]. """)

    with open("crypted.txt", "r") as file:
        crypted = file.read().strip()

    #with open("crypted.txt", "w") as file:
    #   crypted = file.write(crypted)
    
    print(crypted)


    Crypter().brute(crypted)
