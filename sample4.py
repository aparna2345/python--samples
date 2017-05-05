from sys import argv
script,from_file,to_file = argv

def write_to_file(line):
    out_file = open(to_file,'w')
    out_file.write(line)

in_file = open(from_file)
in_file.seek(8)
line = in_file.readline()

write_to_file(line)
