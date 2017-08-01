i = 0
numbers = []

for i in range(0,6):
    print "At the top i is %d" %i
    numbers.append(i)
    print "At the bottom i is %d" %i
    print "Numbers now: ", numbers
	
print "The numbers: "

for num in numbers:
    print num
	
print "Let's use function write the .py again."

i = 0
numbers = []

def w_while(i):
    print "At the top i is %d" %i
    numbers.append(i)
    print "Numbers now: ", numbers

w_while(i)
i = i+1	
print "At the bottom i is %d" %i
w_while(i)

i = i+1	
print "At the bottom i is %d" %i
w_while(i)

i = i+1	
print "At the bottom i is %d" %i
w_while(i)

i = i+1	
print "At the bottom i is %d" %i
w_while(i)

i = i+1	
print "At the bottom i is %d" %i
w_while(i)
