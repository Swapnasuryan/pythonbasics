class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("The Rabbit is eating a Carrot")

class Fish(Animal):
     pass

rabbit = Rabbit()
fish = Fish()

rabbit.eat()
fish.eat()












