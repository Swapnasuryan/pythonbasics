#objects as arguments
#class Car:

#    color = None

#class Motorcycle:

 #   color = None

#def change_color(vehicle,color):

#    vehicle.color = color

#car_1 = Car()
#car_2 = Car()
#car_3 = Car()
#bike_1 = Motorcycle()

#change_color(car_1,"Red")
#change_color(car_2,"White")
#change_color(car_3,"Black")
#change_color(bike_1,"Blue")

#print(car_1.color)
#print(car_2.color)
#print(car_3.color)
#print(bike_1.color)

#Duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "if it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

#person.catch(duck)
person.catch(chicken)


















