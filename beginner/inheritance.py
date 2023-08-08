
#inheritance

#class Animal:

 #   alive = True

 #   def eat(self):
 #       print("This animal is eating")

 #   def slumber(self):
 #       print("This animal is sleeping")

#class Rabbit(Animal):
#    def run(self):
#        print("This rabbit is running")
#class Fish(Animal):
 #   def swim(self):
 #       print("This fish is swimmimg")
#class Hawk(Animal):
#    def fly(self):
#        print("This hawk is flying")

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.slumber()

#rabbit.run()
#fish.swim()
#hawk.fly()

#multi-level inheritance = when a derived (child) class inherits another derived (child) class

#class Organism:

#    alive = True

#class Animal(Organism):

#    def eat(self):
#        print("This animal is eating")

#class Dog(Animal):

 #   def bark(self):
 #       print("This dog is barking")

#dog = Dog()
#print(dog.alive)
#dog.eat()
#dog.bark()

#multiple inheritance = child class is derived from more than one parent class

class prey:

    def flee(self):
        print("This animal is flees")

class predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(prey):
    def eat(self):
        print("The rabbit is eating carrot")
class Hawk(predator):
    pass
class Fish(prey,predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
#hawk.hunt()
#fish.flee()
#fish.hunt()
rabbit.eat()












