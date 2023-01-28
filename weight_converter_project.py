#Receiving Input from user
weight = int(input("Enter your weight: "))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":             #Comaring units with making no issue of case sensitivity
    converted = weight * 0.45       #1 kg = .045 pounds
    print(f"You are {converted} kilogram")
else:
    converted = weight / 0.45
    print(f" You are {converted} pounds")
