import random

def main(fileName):
    # Open the file and remove newlines and leading / trailing spaces
    with open(fileName, "r") as file:
        data = [i.strip() for i in file.readlines()]

    # Find the random stuten by first picking an index
    indx = random.randint(0, len(data) - 1)
    student = data[indx]

    # Other way of doing it
    student = random.choice(data)
    indx = data.index(student)

    # Tell the user who won/lost
    print(f"The random stutent was: {student} of index {indx}")

if __name__ == "__main__":
    main("navne.txt")

