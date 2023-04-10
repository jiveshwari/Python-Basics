def temp(value):
    if value >= 7:
        return "Warm"
    else:
        return "Cold"

value = float(input("Enter temp :"))
print(temp(value))