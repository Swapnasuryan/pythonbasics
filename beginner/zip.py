# zip(*iterables) = aggregates elements from two or more iterables(list,tuples,sets,etc.)
#                   creates a zip object with paried elements stored in tuples for each elemnts

#usernames = ["Sonu","Nagu","Mister"]
#passwords = ["p@sswors","abc124","guest"]
#login_date = ["1/1/2023","1/2/2023","1/3/2023"]
#users = zip(usernames,passwords)
#users = list(zip(usernames,passwords,login_date))
#users = dict(zip(usernames,passwords,login_date))
#print(type(users))
#for key,value  in users.items():
#    print(key+ " : "+ value)
#for i in users:
#    print(i)

# ****************************************************************
# if __name__ == '__main__'
# ****************************************************************

# y tho?
# 1. module can be run as a standalone program
# 2. module can be imported and used by other modules

# python iterpreter sets "special variables", one of which is __name__
# then python will excute the code found within __main__ if its the initial module being run

#print(__name__)
#import module_prac
#print(module_prac.__name__)



def hello():
    print("hello")


if __name__ == '__main__':
    hello()
#    print("running this module directly")
#else:
#    print("running the module indirectly")

















