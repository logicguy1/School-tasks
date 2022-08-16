# Define a dict
## {KEY: VAL}
students = {"Hans" : 7, 
            "Ole" : 4,
            "Peter" : 10,
            "Nina" : 12}

print(students["Ole"]) # Read value from dict
## 4

students["Jesper"] = -3 # Add something to the dict
print(students)
## {"Hans":7,"Ole":4,"Peter":10,"Nina":12,"Jesper":-3}
##                                       ^^^^^^^^^^^^

students["Hans"] = 12 # Edit a value
## {"Hans":12,"Ole":4,"Peter":10,"Nina":12,"Jesper":-3}
##  ^^^^^^^^^

# Loop over dict
for name, grade in students.items():
    print(name, grade)

# Loop over keys
for key in students.keys():
    print(key)

# Loop over values
for value in students.values():
    print(value)

