# filter() = create a collection of a elements from an iterable for which a function returns true

# filter(function, iterable)

#friends = [("uma",19),
#           ("maheshwari",18),
#           ("Narendra",17),
#           ("Anirudh",16),
#           ("Haritha",21),
#            ("Preet",20)]

#age = lambda data: data[1] >= 18

#chilling_buddies = list(filter(age,friends))

#for i in chilling_buddies:
#    print(i)

#reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#           performs function on first two elements and repeats process until 1 value remains

#reduce(function, iterable)

import functools
#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x,y:x+y,letters)
#print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorial)
print(result)


















