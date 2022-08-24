"""

TASK: Create a frequency analasys program for breaking substetution chiffers

"""

import math

frequency = {
        "A": 6.01, "B": 1.41, "C": 0.29, "D": 7.24, "E": 16.70, "F": 2.27, 
        "G": 4.56, "H": 1.88, "I": 5.55, "J": 1.11, "K": 3.07, "L": 4.85, 
        "M": 3.40, "N": 7.55, "O": 4.14, "P": 1.33, "Q": 0.01, "R": 7.61, 
        "S": 5.67, "T": 7.03, "U": 1.85, "V": 2.88, "W": 0.002, "X": 0.02, 
        "Y": 0.72, "Z": 0.02
    }


def create_barchart(data, myKey, alph):
    display = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse = True)}
    out = ""
    maxItem = list(display.items())[0][1] # Get the higest procentage
    height = 10 
    multiplier = height / maxItem # What we should multiply with to make the higest be 100%

    for i in range(height, 0, -1):
        count = 0 

        for key, val in display.items(): # Get the amount of pipes to append
            count += 1 if val * multiplier >= i else 0

        out += "┃" * count
        out += "\n"

    out += "".join([f"{alph[myKey.index(key)]}" for key, val in display.items()])
    out += f"\n{'↑'*len(display.items())}\n"
    out += "".join([f"{key}" for key, val in display.items()])

    print(out)

def decrypt(key, alph, data):
    data = data[:60]
    print("Data input preview: ", data, "\nData output preview: ", end = "", flush = True)
    for i in data:
        try:
            print(alph[key.index(i)], end = "", flush = True)
        except ValueError:
            print(i, end="", flush=True)

    print()

def analyse(data):
    analasys = {}

    alph = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
    
    # Initialise the dict
    for i in alph:
        analasys[i] = 0

    # Count the letters in the data
    length = 0 
    for i in data:
        try:
            analasys[i] += 1
            length += 1 # Count how many normal charecters are in the list
        except KeyError:
            continue

    # Calculate the procentages of each letter
    procLetter = {}
    for letter, count in analasys.items():
        procLetter[letter] = round(count / length * 100, 2)

    print("Analasys output:", procLetter)

    myKey = []
    alph = []
    taken = [] # Only want to allow each letter to be defined once
    for key, val in frequency.items():
        # Find the lowest posible diffrence in procentages
        diffs = [(ltr, proc, abs(proc - val)) for ltr, proc in procLetter.items() if ltr not in taken]
        if len(diffs) != 0:
            item = min(diffs, key=lambda x: x[2]) # Get the letter with the biggest acuracy
        else:
            item = ("╳", 0, 0)

        taken.append(item[0])
        myKey.append(item[0])
        alph.append(key)

        print(item[0], "->", key, "... Error:", round(item[2], 1), "% off", val)

    print("Approximated key: ", myKey)
    
    decrypt(myKey, alph, data)
    create_barchart(procLetter, myKey, alph)


if __name__ == "__main__":
    with open("chiffer.txt", "r") as file:
        data = file.read().upper()

    analyse(data)
