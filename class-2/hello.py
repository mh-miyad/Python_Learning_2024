# #  Start learning variable 

# # x,y,z = "Orange", "Banana", "Cherry"
# # print(x,y,z)
# # # here i can see that 
# # x="Mango"
# x = str(3)    # 
# y = int(3)
# z = float(3)  # 

# print(x,y,z)
# #  how check type of variable by type() function
# print(type(x))
# #  End here  variable part  ""
"""
Python variables hold data of different types
Object type or data type 
1.Number
1.1.Integer
1.2.Float
1.3.Complex
2.List
3.Dict
4.Tuple
5.Boolean
6.String
7.Set
8.File
9.NoNe
"""
# ! Start here Number method 
"""
1.append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
==========================================
2.insert()

Inserts an element at a specific index in the list.
Does not return a value.
my_list = [1, 2, 3]
my_list.insert(1, 5)  # Insert before index 1 (second position)
print(my_list)  # Output: [1, 5, 2, 3]
=============================================
3.remove()
Removes the first occurrence of an element from the list.
Raises a ValueError if the element is not found.
Does not return a value.
my_list = [1, 2, 3, 2]
my_list.remove(2)  # Removes the first occurrence of 2
print(my_list)  # Output: [1, 3, 2]
====================================
4.sort()

Sorts the elements of the list in ascending order (by default).
The original list is modified in place.
Optional reverse=True parameter for descending order.
my_list = [3, 1, 4, 2]
my_list.sort()  # Sorts in ascending order
print(my_list)  # Output: [1, 2, 3, 4]

my_list = [3, 1, 4, 2]
my_list.sort(reverse=True)  # Sorts in descending order
print(my_list)  # Output: [4, 3, 2, 1]
===========================================
5.index()

Returns the index (position) of the first occurrence of an element in the list.
Raises a ValueError if the element is not found.
my_list = [1, 2, 3, 2]
index_of_2 = my_list.index(2)  # Find the index of 2
print(index_of_2)  # Output: 1
===========================================
6.count()

Counts the number of occurrences of an element in the list.
Returns the count.
my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)  # Count the occurrences of 2
print(count_of_2)  # Output: 2
==========================================
Adding/Removing Elements:

clear(): Removes all elements from the list.
pop(): Removes and returns the element at a specific index (or the last element by default).
extend(): Adds all elements from an iterable (like another list) to the end of the list.
reverse(): Reverses the order of elements in the list (in place).
Accessing and Iterating:

len(): Returns the number of elements in the list.
copy(): Returns a shallow copy of the list.
index(): Finds the index of the first occurrence of an element.
count(): Counts the number of occurrences of an element.
enumerate(): Returns an iterator yielding pairs of (index, element) from the list.
Modifying Contents:

sort(): Sorts elements in place (ascending by default, with optional parameters for custom sorting).
reverse(): Reverses the order of elements in place.
pop(): Removes and returns the element at a specific index (or the last element by default).
del: Removes an element at a specific index.
Advanced Operations:

any(): Checks if any element in the list evaluates to True.
all(): Checks if all elements in the list evaluate to True.
min(): Returns the smallest element.
max(): Returns the largest element.
set(): Creates a set from the unique elements of the list.
"""



# ! End here Number method 
