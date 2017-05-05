def sample(first_name,last_name):
    out_file = open("b.txt", 'w')
    out_file.write("his full name is "+ first_name + " " + last_name)
    out_file.close()
def print_all(first_name):
    print(f"His first name is {first_name}")

print("enter your first name: ")
first_name = input()
print("enter your last name:")
last_name = input()
sample(first_name,last_name)
print_all(first_name)
