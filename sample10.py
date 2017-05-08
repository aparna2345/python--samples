print("enter number 1:")
first = input()
print("enter number 2:")
second = input()
print("enter number 3:")
third = input()
if first < second:
    if first < third:
        print (f" {first} is the smallest")
    else :
        print(f"{third} is the smallest")
else:
    if second < third:
        print("{second} is the smallest")
    else:
        print (f"{third} is the smallest")
