array = {}
i = 0
a = input("Enter the number of students: ")
while i < int(a) :
    i=i+1
    print(f"enter the  name of student {i}:",end=" ")
    student = input()
    print(f"enter the mark of student {i}:",end=" ")
    mark = input()
    array[student] = mark
print(array)

print("enter the name of student to retrive name")
name = input("enter the name ")
print(array[name])
