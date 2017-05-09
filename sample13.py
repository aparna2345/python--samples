i = 0
a = input("Enter the number: ")
numbers = []
while i < int(a):
    print(f"enter number {i}:",end =' ')
    i=i+1
    b=input()
    numbers.append(b)

small = numbers[0]
for number in numbers:
    if small > number:
        small = number
print(f"the smallet number is {small}")
