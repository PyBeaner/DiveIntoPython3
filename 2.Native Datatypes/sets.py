__author__ = 'PyBeaner'

# Creation
a_set = {1}
print(a_set,type(a_set))
a_list = [1,2,3]
print(set(a_list))
# empty set
a_set = set()
print(type(a_set))
a_dict = {} # if empty,it's a dictionary(historical reason)
print(type(a_dict))

# Modification
a_set = {1,2}
a_set.add(4)  # add anything hashable
print(a_set)
a_set.add(4)
print(a_set)  # does not add existing item(no-op)
a_set.update([1,2,5],{3,6},(5,7)) # update elements from iterable
print(a_set)

# Removing
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
a_set.discard(1)
print(a_set)
a_set.discard(1)  # do nothing if item not exist
print(a_set)
# a_set.remove(1)  # KeyError
# using pop
a_set.pop()  # arbitrary popping(set is unordered)
print(a_set)
a_set.clear()  # Empty set
# a_set.pop()  # KeyError

# Set Operations
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
print(3 in a_set)
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
c_set = a_set.union(b_set)  # union returns a new set
print(c_set)
c_set = a_set.intersection(b_set)
print(c_set)
c_set = a_set.difference(b_set)
print(c_set)
c_set = a_set.symmetric_difference(b_set) # all elements that only occurs once
print(c_set)
# three of methods are symmetric
symmetric = b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)
print(symmetric)
symmetric = b_set.union(a_set) == a_set.union(b_set)
print(symmetric)
symmetric = b_set.intersection(a_set) == a_set.intersection(b_set)
print(symmetric)
# not symmetric
symmetric = a_set.difference(b_set) == b_set.difference(a_set)
print(symmetric)
# sets relationship
a_set = {1,2,3}
b_set = {1,2,3,4}
print(a_set.issubset(b_set))
print(b_set.issuperset(a_set))
