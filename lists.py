#!/python/3

"""There are 4 collection data types -
1. lists
2. Tupple
3. Set
4. dictionary"""

thislist = ["pikachu","chikorita","togapi","charlizard","jiggly puff","si duck"]
print(thislist)
print(thislist[1])
print(thislist[-1]) # This is negative indexing. It means beginning from the end
print(thislist[2:5])
print(thislist[:-4])
thislist[1] = "ash"
print(thislist)

#Loop in lists

for x in thislist:
	print(x)

#if condition in the list

if "ash" in thislist:
	print("ash is in the list of pokemons")

#append, insert, remove the list with something
thislist.append("something")
print(thislist)
thislist.insert(2,"blue")
print(thislist)
thislist.remove("blue")
print(thislist)

#copy a list
newlist = list(thislist)
print(newlist)

#Join two lists
list3 = newlist + thislist
print(list3)

#The list() constructor
thislist = list(("red","blue","orange"))
print(thislist)