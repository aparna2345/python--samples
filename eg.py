import random
fruits = ["apple","orange","mango","pineapple","grapes","banana","sappota"]
selected = random.choice(fruits)
print(len(selected))
array = list(selected)
#print(array)
i = 0
while i <len(selected):
     print(" - ",end=' ')
     i=i+1
print("enter the letter")
