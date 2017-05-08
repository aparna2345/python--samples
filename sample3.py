from sys import argv
script, from_file, to_file = argv
print(f"copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()
print("enter your name")
name=input(">")

out_file = open(to_file, 'w')
out_file.write(indata+"this is done by "+ name)
out_file.close()
in_file.close()
