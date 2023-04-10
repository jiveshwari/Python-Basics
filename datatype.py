#!/python/3

b = 5
a = 35e3
print(type(b))
print("a = ", a)

#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print("x = ", x)
print("y = ", y)
print("z = ", z)

#conversation of one data type to another

i = 4
j = 2.9

i = float(i) #int 4 converted into a float
print(i)

j = int(2.9) # float is converted into a integer
print(j)

j = str("let's see if this works")
print(j)
