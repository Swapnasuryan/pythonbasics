#type casting = convert the data type of a value to another data type

#X = 1    #int
#Y = 2.0  #float
#Z = 3    #string

#Y = int(Y)
#Z = float(Z)
#X = str(X)

#print(X*3)
#print(Y)
#print(Z*3)

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
print("Hello " +name)
print("you are "+str(age)+" years old")
print("you are "+str(height)+" tall")
