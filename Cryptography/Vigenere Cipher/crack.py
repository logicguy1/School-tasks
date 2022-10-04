from typing import Dict

import config as conf


class Cracker:
    def __init__(self, text):
        self.text = text

    def get_frequency(self, text: str) -> Dict[str,int]:
        data = {k: 0 for k in conf.alph}

        for i in text:
            try:
                data[i] += 1
            except KeyError:
                pass

        return data

    def analasys(self, keyLen: int) -> None:
        """ Return a frequency table for the specified keylen """

        for i in range(keyLen):
            print(self.text[i::keyLen][:30])
            analasys = self.get_frequency(self.text[i::keyLen])
            print(dict(sorted(analasys.items(), key=lambda item: item[1])))

if __name__ == "__main__":
    with open("data.txt", "r") as file:
        Cracker(file.read().strip()).analasys(3)
