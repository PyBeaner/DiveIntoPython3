__author__ = 'PyBeaner'

# Tuple: immutable list
a_tuple = (1,2,3)
# append/remove/pop raises AttributeError
a_tuple.index(1)
print(2 in a_tuple)

# use tuple:
# faster than list;write-protect data;using as a dictionary key(because of its immutability)

# Boolean checking
from number import is_it_true
print(is_it_true(()))
print(type((False)))  # Boolean
print(type((False,)))  # Tuple


# assign values
v = ("a",2,True)
x,y,z=v
print(x,y,z)
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
# [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY] = range(7)
print(MONDAY,TUESDAY)  # 0,1
