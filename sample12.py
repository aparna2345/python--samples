numbers = [12,1,3,123,2,4,5]
small = numbers[0]
for number in numbers:
    if small < number:
           small=number
print(f"the smallet number is {small}")
