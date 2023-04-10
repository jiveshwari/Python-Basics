#!/python/3

#Python set

thisset = {"a","b","c"}
print(thisset)
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)
print(len(thisset))
thisset.discard("banana") #no remove
print(thisset)

#Join 2 sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Set as a constructor

set = set(("yo","bye"))
print(set)

#Python Dictionary

thisdict = {
	"brand": "DW",
	"model": "watch",
	"price": "12000"
}
print(thisdict)
x = thisdict["model"]
y = thisdict.get("model")
print(x)
print(y)

for x, y in thisdict.items():
  print(x, y)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
	print("Noooooo")

thisdict["color"] = "rose gold"
print(thisdict)

mydict = thisdict.copy()
print(mydict)

#Nested Dictionary

myfamily ={
	"child1": {
		"age":"12",
		"name": "Sam"
	},
	"child1=2": {
		"age":"2",
		"name": "Emma"
	}
}
print(myfamily)

thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)


