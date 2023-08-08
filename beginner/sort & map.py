# sort() method = used with lists
# sort() function = used with iterables

#students = ["Swapna","Suryan","Nagendra","Sachin","Sundar"]

#students.sort(reverse=True)
#sorted_students = sorted(students,reverse=True)
#for i in sorted_students:
#    print(i)

#students = [("Swapna","F",60),
#            ("Suryan","A",33),
#            ("Nagendra","D",36),
#            ("Sachin","B",20),
#            ("Sundar","C",78)]
#grade = lambda grades:grades[1]
#students.sort(key=grade,reverse=True)
#for i in students:
#    print(i)
#students = (("Swapna","F",60),
#            ("Suryan","A",33),
#            ("Nagendra","D",36),
#            ("Sachin","B",20),
#            ("Sundar","C",78))
#grade= lambda grades:grades[1]
#sorted_students = sorted(students,key=grade)
#for i in sorted_students:
#    print(i)

# Map() = applies a function to each item in an iterable(list,tuple,etc)

# Map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_rupees = lambda data: (data[0]),data[1]*81.75)

store_rupee = list(map(to_rupees,store))

for i in store_rupee:
    print(i)























