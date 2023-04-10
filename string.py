#!/python/3

a = """I am jiya,
we are practicing strings here"""

array = "I, am , an, array"

print(a)
print(array[4])

#string length
str = "STring I am"
print(len(str))

#strings method
b = "Methods of string"
print(b.strip())
print(b.lower())
print(b.upper())
print(b.replace("Methods","Bello"))
print(b.split())

#check if some text is in the strings or not
txt = "I am check string, Cool"
x = "bello" in txt
print(x) #boolean output

#string concatanation (connect two string)
d = "Bello says"
e = " a minion"
print(d+e) # we cannot combine strings and numbers

#combine strings and numbers using format
f = "You know how old jadoo is {}"
g = 5
print(f.format(g))

#use of format() with multiple numbers
h = "That cupcake is {}% yumm, {}% beautifull and {}% my life"
i = 654
j = 860
k = 765
print(h.format(i,j,k))

#Escape character

l = "Joey said \"I am \"Sorry\"\""
print(l)
