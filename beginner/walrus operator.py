#walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part pf a larger expression

#happy = True
#print(happy)

#print(happy := True)
foods = list()
while True:
    food =input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

#foods = list()
#while food := input("What food do you like?: ") !="Quit":
#    foods.append(food)