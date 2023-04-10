#!/python/3

thistuple = ("a","b","c") #Tuples are unchangeable, or immutable
print(thistuple)

for x in thistuple:
	print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
	print("No bro not found!")