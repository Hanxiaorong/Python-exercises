from sys import argv

script, input_file = argv

def print_a_line(line_count, f):
    print line_count, f.readline()
	
print "Let's print three lines:"

current_file = open(input_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)
