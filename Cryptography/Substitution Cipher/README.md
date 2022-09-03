# Substetution chiffer

The program (`main.py`) takes a file (`chiffer.txt`) containing eather the plaintext or chiffered text

To change the mode, swap the `#` at this part

```py
  58   │ 
  59   │     with open("chiffer.txt", "r") as file:
  60   │         chiffer = crypt.encrypt(file.read())
  61   │         # chiffer = crypt.decrypt(file.read())
  62   │
```

## Requrements

This program has the following reuirements

- [Colored](https://pypi.org/project/colored/)  
  `pip install colored`

## The main program

To run the main decryption tool, you want your local path to be in `./Cryptography/Substitution Cipher` and you run the following command

```bash
python -m crypter
```

This will take you to the main menu where you can search the crypted text and you can use the varius features to work yourself towards the key

### 1: Lookup a word in the database

Using this we can look for words matching a pattern

#### The rules for creating patters

To create a pattern we can tell it that there is a unknowen letter at this spot

eg.

```py
>> DE_

## 0. DER, 1. DET, 2. DEN, 3. DEM, 4. DEL
```

We can also tell it that we are expecting two similar letters by using numbers (always start with 0)

eg.

```py
>> I__E

## 0. IKKE, 1. INDE, 2. IGLE, 3. ISME, 4. ISNE, 5. ISSE

>> I00E

## 0. IKKE, 1. ISSE
```

### 2. See likely matches in the database

This features will make the program analyse the text and tell you what likely connections it can make

Once you boot it up it will ask you how sentensive it should be, if you dont have a lot of letters i suggest 2 - 3 where as you can use your own good judgement

Running it might take a second

It will display the shortes letters first, these are more likey to be acurate

It wil show a result that looks like this

```

crypted text: the pattern created -> results found      an example with context

```

It will also tell you the amount of matches made, this number should not drop once adding a new letter, might drop slighty but it should find more matches with the new letter in place ;)

At the bottom it shows you the amount of times each letter swap took place, you can use these to your advantage

### 3. Frequency analasys

This executes a frequency analasys, you might want to use only the first few letters as it very quickly becomes inacuate

The output will look like this:

```

Plain letter - count it appared    the corosponding letter from at table at 

```

### 4. Exit the program

This exits the program, lol

### How do i edit the key?

In the local path `./Cryptography/Substitution Cipher/crypter` there is a file `crypto.py`, this is where we can modify and change the key as much as we want


```py

  14   │     def __init__(self, text) -> None:
  15   │         self.text = text
  16   │         self.alph = conf.alph
  17   │         self.key = {
  18   │                 "U": "E",
  19   │                 "T": "A",
  20   │                 "J": "I",
  21   │                 "D": "L",
  22   │                 "E": "R",
  23   │                 "H": "S",
  24   │                 "D": "L",
  25   │                 "E": "R",
  26   │                 "R": "O",
  27   │                 "A": "G",
  28   │                 "X": "V",
  29   │ 
  30   │                 "I": "M",
  31   │                 "K": "N",
  32   │                 "Y": "D",
  33   │                 "B": "T",
  34   │                 "F": "F",
  35   │                 "Q": "H",
  36   │                 "Z": "P",
  37   │                 "L": "U",
  38   │                 "V": "B",
  39   │                 "O": "J",
  40   │                 "W": "K",
  41   │                 "S": "Y"
  42   │             }
  43   │         self.ordbog = Ordbog()

```

## Roadmap

1. Allow the user to modify the key without exiting
   Drawbacks: They key might get currupt or otherwise lost if the program crashes
