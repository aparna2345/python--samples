i = 0
print("enter the sentance :")
line = input()
name = []
array= line.split(' ')
for word in array:
    if word != "is" and word !="the" and word != "of":
        #print(word)
        name.append(word)
name.pop(len(name)/2+1)
print(name)

#while i<len(array):
#    if array[i] != "is":
#        print(array[i],end='  ')
#    i=i+1
