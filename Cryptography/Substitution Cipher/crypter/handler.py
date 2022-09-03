"""

Program to clean datasets

"""

import random

alph = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")

with open("ordliste.txt", "r") as file:
    data = []
    for x in file.readlines():
        for i in x.split(" "):
            i = i.strip().upper()
            i = i.split("/")[0]

            print([i for i in i.strip() if i not in alph])
            if len([i for i in i.strip() if i not in alph]) != 0 or i == "" or i in data:
                continue # Ignore the word

            data.append(i)

with open("ordliste.txt", "w") as file:
    random.choice(data)
    file.write("\n".join(data))
    print(i)
