#scope = the region that a variable is recognized
#        a variable is only available from inside the region it is created.
#        a global and locally scoped versions of a variable can be created

#name = "Suryan"  # global scope (available inside & outside function)
#def display_name():
 #   name = "Swapna"   # local scope (available only inside this function)
#    print(name)
#display_name()
#print(name)

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

#def add(*args):
 #   sum = 0
 #   args = list(args)
 #   args[0] = 0
 #   for i in args:
 #       sum +=i
 #   return sum

#print(add(6,5,6,7))

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword argument

#def hello(**kwargs):
#   #print("Hello " +kwargs['first'] + " " + kwargs['last'])
#    print("Hello",end=" ")
#    for key,value in kwargs.items():
#        print(value,end=" ")
#hello(title= "Mrs.", first="Swapna",middle= "Nagendrarao",last= "suryan")









