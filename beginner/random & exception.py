import random

#x = random.randint(1,6)
#print(x)

#y = random.random()
#print(y)

#mylist = ['rock','pepper','scissors']
#Z = random.choice(mylist)
#print(Z)

#cards = [1,2,3,4,5,6,7,8,9,"J","Q","K"]
#random.shuffle(cards)
#print(cards)

#exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
   # print(result)
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This will always execute")










