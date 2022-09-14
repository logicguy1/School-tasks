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

    #crypted = Crypter(5).encrypt(r"""Der var en gang en fyr der sage at han gerne ville agere i en verden ude bøvl og larm, dog kom gud og sage at dette ikke ville være en mulighed lige PT, man kan jo også undre sig over hvorfor gud skulle være sådan en lysseslukker? Man skulle jo tro han var brandmand men med elektricitet Lydsystemet for dansk har et rigt vokalinventar, hvor der skelnes mellem 16-18 forskellige vokalkvaliteter. Desuden skelnes der mellem korte, lange og stødte vokaler. Også konsonanterne har deres variation, og de danske konsonanter svækkes i stavelsesfinal position. Det gør, at der findes flere såkaldt vokoide konsonanter som i fx mad ~ maæ, hav ~ hau og mor ~ moå. Det tryksvage e, schwa, smelter ofte sammen med nabolyde (schwa-assimilation) som derved bliver stavelsesbærende. Den danske udtale kan være svær at håndtere for udlændinge. Velkendt er rødgrød med fløde, en uklar grænse mellem vokaler og konsonanter som skaber lange vokaliske sekvenser, ligesom i røget ørred. De danske dialekter har ét, to eller tre grammatiske køn, og kendeordet kan være efterhængt eller foranstillet. På Færøerne findes den særlige skriftsprogsnære udtaleform gøtudansk, i Sydslesvig sydslesvigdansk. De traditionelle dialekter er på retur og erstattes efterhånden af et landsdækkende rigsdansk, men udtalen varierer stadig i landets egne. Et kendetegn ved det vestjyske er stød, mens specielt sproget på Fyn, Lolland og Falster samt på Bornholm synes at ligne mere (d)et syngende svensk(e). Således har nogle syddanske dialekter musikalsk accent. Socialt betingede udtaleforskelle, sociolekter, er (eller var engang) mest velkendt fra Københavnerområdet – det borgerlige højkøbenhavnske, senere rigsdansk, og arbejderklassens lavkøbenhavnske, gadesproget. Sprogfællesskaber markeres af en genkendelig sprogform, det være sig i udtale eller grammatik, og medlemmer fra andre sprogfællesskaber end det danske kan så bære disse kendemærker med i deres danske sprogudtale, og det kaldes også en etnolekt. Det hører alt sammen med til det levende sprog. Dansk påvirker også andre sprog. Således findes der danske påvirkninger i de nordfrisiske dialekter i Sydslesvig (f. eks. ej og ikke → ai på Mooring, ei i Fering og Öömrang og ek på Sölring, dreng → dring på Fering, Öömrang og Mooring og dreeng på Sölring; ild → ial på Før og Amrum, iilj i Bøkingherred)[10][11]. Da Gotland var dansk i årene 1361 til 1645 kom der også mange danske låneord ind i gutamålet (gutnisk). Eksempler. som findes endnu i dag, er någle (dansk nogle, svensk några), saktens (dansk sagtens, svensk nog visst) eller um en trent (dansk omtrent, svensk ungefär)[12]. """)

    with open("crypted.txt", "r") as file:
        crypted = file.read().strip()

    #with open("crypted.txt", "w") as file:
    #   crypted = file.write(crypted)
    
    print(crypted)


    Crypter().brute(crypted)
