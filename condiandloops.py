#!/python/3

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

i = 1
while i < 6:
  print(i)
  i += 1

i = 0
while i<3:
	i = i+1
	print(i)
	if i==3:
		print(i)
	continue
	print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in fruits:
  if x == "banana":
    continue
  print(x)
