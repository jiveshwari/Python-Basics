#!/python/3

#Boolean values

print(213>2)
print(2 == 2)
print(2321 != 2321)
print(3>4123)

#if-else condition

a = 2
b = 4

if(a == b):
	print(" a and b are same omg!")
else:
	print("Told you! a is not equal to b")

#evaluate boolean

c = 5
d = 4
print(bool(c+d))

"""Most values are TRUE in boolean like 
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""

#False Boolean

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Functions can return a boolean duh!

def myfunction() :
	return True

print(myfunction())

"""Built in function : Python also has many built-in functions that returns a boolean value, 
like the isinstance() function, which can be used to determine if an object is of a certain data type"""

e = "Yo! I am a built in function"
print(e)
print(isinstance(e, int))
