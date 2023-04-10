#!/python/3

i_am_first_var = 3
print(i_am_first_var)

vartwo = 2
print(vartwo)
vartwo = "2 is changed into a string! Cool!" #Variables do not need to be declared with any particular type and can even change type after they have been set.
print(vartwo)

#Legal variable names:
myvar = "I am myvar"
my_var = "I am my_var"
_my_var = "I am _my_var"
myVar = "I am myVar"
MYVAR = "I am MYVAR"
myvar2 = "I am myvar2"

#Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Let's print the legal variable shall we?
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(myvar)
print(MYVAR)
print(myvar2)

#use the + character to add a variable
x = "Jiya"
y = " is awesome"
z = x + y
print(z)

#Global variable demo

g = "Global af"

def myfun():
	i = "internal var"
	global k
	k = "I am a var inside the function but with a global keyword so I am global af again"
	print(g)
	print(i)
	print(k)

myfun()

print(k)