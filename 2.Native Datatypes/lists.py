# coding=utf8
__author__ = 'PyBeaner'

# indexing
a_list = ['a','b','mpilgrim','z','example']
print(a_list)
print(a_list[4])
# negative index:alist[-n] = alist[length-n]
print(a_list[-1])

# slicing
print(a_list[1:3])
print(a_list[1:-1])
print(a_list[:2])
print(a_list[2:])
print(a_list[:])

# adding items
a_list = ['a']
a_list += [2.0,3]
print(a_list)
a_list.append(True)
print(a_list)
a_list.extend(["four",'Ω'])
print(a_list)
a_list.append(["four",'Ω'])# append any object as an item
print(a_list)

# searching
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
a_list.count("new")
print("new" in a_list)# slightly faster than "count"
# ValueError
# WHY:"-1" can be an index,so..
# print(a_list.index('cc'))


# removing
del a_list[0]
print(a_list)
a_list.remove("new")# only remove the first one,and raise ValueError like the "index" method ,if the item not in it
print(a_list)
# using pop
a_list.pop()# Default:post the last
print(a_list)
# [].pop() #IndexError:pop from empty list

# boolean
import number
number.is_it_true([])
number.is_it_true(["a"])
number.is_it_true([False])


