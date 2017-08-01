from sys import argv

script, filename = argv
target = open(filename,'w')

print "We will write three lines."
line1 = raw_input('>')
line2 = raw_input('>')
line3 = raw_input('>')

print "Ok, I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
