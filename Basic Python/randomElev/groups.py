"""

From a list, group items randomly of a size of n

"""

import random

def generate_groups(arr:list, lmt:int):
    """
    Group items in a list
    Takes: 
           arr (array of stutent names)
           lmt (size of groups)
    """
    random.sluffle(arr) 

    groups = [] 
    for i in range(0, len(arr), lmt):
        groups.append(arr[i:i+lmt]) 

    return groups


def main(fileName):
    with open(fileName, "r") as file: 
        data = [i.strip() for i in file.readlines()] 

    groups = generate_groups(data, int(input("Hvor store grupper skal det være?\n>> "))) 

    for i in groups: 
        print(", ".join(i))

if __name__ == "__main__":
    main("navne.txt")

