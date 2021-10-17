lucky_numbers = [4,7,36,76,15, 77]
friends = ["Kevin", "Karen", "Jim", "John", "John", "John", "Anne"]

# print(friends)  #print all elements

# friends.extend(lucky_numbers)  #add one list to another
# print(friends)

# friends.append("Creed")  #add item to the end of list
# print(friends)

# friends.insert(1, "Kelly")   #insert value to position 1 and push other elements to the right
# print(friends)

# friends.remove("Jim")  #JIM is removed
# print(friends)

# friends.clear()  #empty list
# print(friends)

# friends.pop()  #last item has been removed
# print(friends)

#print(friends.index("Kevin"))  #check what is the index of value

#print(friends.count("John"))  #count the number of those elements in the list

# friends.sort()  #sort in ascending order
# lucky_numbers.sort()
# print(friends)
# print(lucky_numbers)


lucky_numbers.reverse()  #reverse the order
print(lucky_numbers)

friends2 = friends.copy()  #create a copy of list
print(friends2)
