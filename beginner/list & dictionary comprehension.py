# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression (if/else) for item in iterable]

#squares = []                    # create an empty list
#for i in range(1,11):             # create a for loop
#    squares.append(i*i)         # define what each loop iteration should do
#print(squares)

#Squares = [i*i for i in range(1,11)]
#print(Squares)
#cubes = [i*i*i for i in range(1,11)]
#print(cubes)


#students = [100,90,80,70,60,50,40,30,0]
#passed_students = list(filter(lambda x:x >= 60,students))
#print(passed_students)

#passed_students = [i for i in students if i>=60]
#print(passed_students)
#passed_students = [i if i>=60 else "FAILED" for i in students]
#print(passed_students)

# dictionary comprehension =  create dictionaries using an expression
#                             can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditions}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
#___________________________________________________________________________________

#cities_in_F = {'New Delhi': 32, 'Hyderabad': 75,'Bengaluru': 100,'Jaipur': 50}

#cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)

#______________________________________________________________________________________

#weather = {'Jammu':"snowing", 'Hyderabad':"sunny",'Bengaluru':"cloudy",'Jaipur':"sunny"}
#sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
#print(sunny_weather)
#____________________________________________________________________________________

#cities = {'New Delhi': 32, 'Hyderabad': 75,'Bengaluru': 100,'Jaipur': 50}
#desc_cities = {key: "Warm" if value >=40 else "Cold" for (key,value) in cities.items()}
#print(desc_cities)
#______________________________________________________________________________________-

def check_temp(value):
    if value >=70:
        return "Hot"
    elif 69>= value >=40:
        return "Warm"
    else:
        return "Cold"
cities = {'New Delhi': 32, 'Hyderabad': 75,'Bengaluru': 50,'Jaipur': 100}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)



















