def main():
    age = int(input("Hvad er din alder??? HUH=!!==!1\n>> ")) 
    if age < 16:
        print("Nonono bad boii")
    elif age < 18:
        print("Op til 16.4%")
    else:
        print("Have fun")a

    main()

# main()

print(["no" if i < 16 else "16.4" if i < 18 else "Hav fun" for i in (int(input("age: ")),)][0])
