from sys import argv

script, filename = argv

print "Opening the file ..."
target = open (filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1 : ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

print "I'm going to write these to the file."

target.write(line1) 
target.write("\n") 
target.write(line2)
target.write("\n") 
target.write(line3) 
target.write("\n")  # 用一个target.write () 将line1, line2, line3 打印出来不会

print "And finally, we colse it."
target.close()