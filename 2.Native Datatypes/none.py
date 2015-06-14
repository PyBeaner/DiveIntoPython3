__author__ = 'PyBeaner'

# None is not the same as False. None is not 0.
# None is not an empty string.
# Comparing None to anything other than None will always return False.
# You can assign None to any variable, but you can not create other NoneType objects
# All variables whose value is None are equal to each other

print(type(None)) # NoneType
print(None==False) # False
print(None==0)
print(None==None) # True
x = None
print(x==None) # True
y = None
print(x==y) # True