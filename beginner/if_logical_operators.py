#if statement = a block of code that will execute if its condition is true

#age = int(input("How old are you?:"))
#if age ==100:
#    print("You are a century old!")
#elif age >= 18:
#print("You are an adult")
#elif age < 0:
#    print("You haven't been born yet")
#else:
#    print("You are a child!")

#logical operatora (and, or, not) = used to check if two or more conditional statement is true

temp = int(input("What is the temperatur outside?: "))

if not(temp>= 0 and temp <= 30):
    print("the temperature is good today!")
    print("go outside")
elif not(temp< 0 or temp >30):
    print("the temperature is bad today")
    print("stay inside")












