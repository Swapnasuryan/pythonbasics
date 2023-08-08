#list = used to store multiple items in a single variable

food = ["pizza", "rice", "dal", "chapati", "curry"]
#print(food)
#print(food[2])
food[0] = "salad"
#print(food[0])
#print(food)
#food.append("ice_cream")
#food.sort()
#food.pop()
#food.remove("rice")
#food.insert(1,"biryani")
#food.clear()

#for x in food:
 #  print(x)

# 2D lists = a list of lists

drinks = ["coffe", "soda", "tea"]
dinner = ["biryani", "chapati", "paneer"]
dessert = ["cake", "ice_cream", "gulab_jamun"]

food = [drinks, dinner, dessert]
print(food[0][1])
print(food[1][0])
print(food[2][2])