#Tuple = collection which is ordered and unchangeble
#          used to group together related data

#student = ("Swapna", 26, "Female")
#print(student.count("Female"))
#print(student.index("Swapna"))

#for x in student:
#    print(x)
#if "Swapna" in student:
#    print("Swapna is Here!")

#set = collection which is unordered, unindexed. No dublicate values

utensils = {"fork", "spoon", "knife"}
#utensils = {"fork","fork", "spoon","knife","knife"}
dishes = {"bowl","plate","cup","spoon"}
#utensils.update(dishes)
dishes.update(utensils)
#print(utensils)
#print(dishes)
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dinner_table = utensils.union(dishes)
#for x in dinner_table:
#    print(x)
#print(utensils.difference(dishes))
#print(dishes.difference(utensils))
#print(utensils.intersection(dishes))

for x in dishes:
    print(x)