import math

#pi = 3.14
#X = 1
#Y = 2
#Z = 3
#print(pi)
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(X,Y,Z,pi))
#print(min(X,Y,Z,pi))

#slicing = create a substring by extracting elements from another string indexing[] or slice()
#            [start:stop:step]

name = "Swapna Suryan"
first_name = name[5]  #start
last_name = name[7:10] #stop
funky_name = name[::2]  #step
reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

website1 = "https://www.google.com/intl/en-US/drive/"
website2 = "https://www.google.com/intl/en-US/drive/features"

#slice = slice(12,-22)
slice = slice(12,-30)
#print(website1[slice])
print(website2[slice])