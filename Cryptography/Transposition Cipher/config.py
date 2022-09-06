from typing import Union

import time
import sys
import os

import colored

# Color variables
F = colored.fg("#ffffff") # White
B = colored.fg("#999999") # Gray
R = colored.fg("#cc2023") # Red

# Alphabeth in use
alph = list("ABCDEFGHIJKLMNOPRSTUVWXYZÆØÅ")

# Function to clear the screen, cross platform
clear = lambda : [print("\n"*40), os.system('cls' if os.name == 'nt' else 'clear')]


def ask(prompt: str, newLine: bool = True, parseInt: bool = False) -> Union[str,int]:
    """ Prompt the user for an input in a unified way """
    
    brk = "\n" if prompt else "" # If there is no prompt, dont add newline before 
    resp = input(f"{F}{prompt}{brk}{B}>> {R}")

    if parseInt:
        if resp.isdigit():
            return int(resp)
        return ask("Your input has to be a number.", newLine = newLine, parseInt = parseInt)

    print(F, end="\n" if newLine else "", flush = True)
    return resp


def highlight(text: str, ltr: str) -> str:
    """ Highligh a specific charecter in a text """
    out = ""

    for i in text:
        if i == ltr:
            out += F + i
        else:
            out += B + i

    return out


def progressbar(it): # Python3.3+
    """ Progress bar """

    print(f"[ {'.'*19} ]", end="", flush=True)

    count = 1
    start = time.time()
    for i, item in enumerate(it):
        yield item

        remaning = round(((time.time()-start) / count) * (len(it)-count), 2)
        amount = count % 20
        print(f"\r[ {'.'*amount}{' '*(20-amount)} ] {count} / {len(it)}, {remaning} s   ", end="", flush=True)
        count += 1

    print("\n", flush=True)


def safe_exit() -> None:
    """ Exit the program """
    sys.exit(0)

