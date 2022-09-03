from typing import List, Dict, Tuple

import config as conf


class Menu:
    """ The menu system, handles displaying options etc """

    def __init__(self, commands: List) -> None:
        self.commands = commands

    def get_choices(self) -> str:
        out: str = ""

        # Show the user what is avaliable to them
        for choice, i in zip(self.commands, range(1, len(self.commands) + 1)):
            out += f"{conf.R}{i}{conf.B}:{conf.F} {choice.__doc__.strip()}\n"

        return out

    def menu(self) -> None:
        while True:
            # Main program loop
            print(self.get_choices())

            choice = conf.ask("", parseInt = True)
            conf.clear()
            self.commands[choice - 1]()


if __name__ == "__main__":
    Menu().menu()
