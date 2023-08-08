#funtion to variable

#def hello():
#    print("Hello")

#hello()
#print(hello)
#hi = hello
#print(hi)
#hi()
#hello()

#say = print
#say("Whoa! I can't belive this works! :o")

# HIgher order function = a function that either:
#                          1. accepts a function as an argument
#                                or
#                          2. returns a function
#                           (in python, functions are also treated as objects)


#def loud(text):
#    return text.upper()

#def quiet(text):
#    return text.lower()

#def hello(func):
#    text = func("Hello")
#    print(text)

#hello(loud)
#hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))












